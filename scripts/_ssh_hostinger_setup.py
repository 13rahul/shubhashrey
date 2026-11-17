"""One-off Hostinger SSH probe + install local public key. Do not commit passwords."""
from __future__ import annotations

import sys
from pathlib import Path

import paramiko

HOST = "46.202.161.182"
PORT = 65002
USER = "u998838607"
PASSWORD = sys.argv[1] if len(sys.argv) > 1 else ""
PUBKEY = Path.home() / ".ssh" / "id_ed25519.pub"


def main() -> int:
    if not PASSWORD:
        print("Usage: python _ssh_hostinger_setup.py <password>")
        return 2
    if not PUBKEY.is_file():
        print(f"Missing pubkey: {PUBKEY}")
        return 1

    pub = PUBKEY.read_text(encoding="utf-8").strip()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting {USER}@{HOST}:{PORT} ...")
    client.connect(
        HOST,
        port=PORT,
        username=USER,
        password=PASSWORD,
        timeout=20,
        allow_agent=False,
        look_for_keys=False,
    )
    print("OK password login")

    def run(cmd: str) -> tuple[int, str, str]:
        stdin, stdout, stderr = client.exec_command(cmd)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return code, out, err

    code, out, err = run("pwd; whoami; hostname; ls -la; ls -la public_html 2>/dev/null | head -n 40; ls -la domains 2>/dev/null | head -n 20")
    print(out)
    if err.strip():
        print("STDERR:", err)

    # Install pubkey if missing
    install = f"""
set -e
mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
PUB='{pub}'
grep -Fqx "$PUB" ~/.ssh/authorized_keys || echo "$PUB" >> ~/.ssh/authorized_keys
echo "authorized_keys lines: $(wc -l < ~/.ssh/authorized_keys)"
"""
    code, out, err = run(install)
    print(out)
    if err.strip():
        print("STDERR:", err)
    if code != 0:
        print(f"key install failed code={code}")
        client.close()
        return 1

    client.close()
    print("Password session closed. Testing key login...")

    client2 = paramiko.SSHClient()
    client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = paramiko.Ed25519Key.from_private_key_file(str(Path.home() / ".ssh" / "id_ed25519"))
    client2.connect(
        HOST,
        port=PORT,
        username=USER,
        pkey=key,
        timeout=20,
        allow_agent=False,
        look_for_keys=False,
    )
    stdin, stdout, stderr = client2.exec_command("echo KEY_OK; pwd")
    print(stdout.read().decode("utf-8", "replace"))
    client2.close()
    print("Key-based SSH works.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
