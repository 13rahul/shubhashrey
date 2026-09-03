# Bhosari MIDC welding-electrode prospect database

Sales outreach dataset for **Bharatweld / Shubhshrey Industries** focused on Bhosari MIDC (Pune 411026).

## Maharashtra MIDC target map (statewide)

| File | Purpose |
|------|---------|
| [Maharashtra_MIDCs_Electrode_Target_Map.xlsx](Maharashtra_MIDCs_Electrode_Target_Map.xlsx) | All MIDC areas by district + electrode demand (High/Medium/Low) |
| [maharashtra-midcs.csv](maharashtra-midcs.csv) | Same data as CSV |

Tabs: README, All_MIDCs, High_Potential, By_District. Rebuild:

```bash
python scripts/build_maharashtra_midcs.py
```

This also refreshes the CRM MIDC dropdown in `includes/geo_data.php`.

## Bhosari prospect files

| File | Purpose |
|------|---------|
| [lookup_tiers.csv](lookup_tiers.csv) | Allowed industry categories, default electrodes, pitch templates |
| [bhosari-midc-prospects.csv](bhosari-midc-prospects.csv) | **Phase 1 master — 100 companies** |
| [bhosari-midc-hot-list.csv](bhosari-midc-hot-list.csv) | Filter: `priority_label = Hot` (start dial/WhatsApp here) |
| [bhosari-midc-deferred.csv](bhosari-midc-deferred.csv) | Extra candidates beyond the frozen 100 |
| [bhosari-midc-parked.csv](bhosari-midc-parked.csv) | Non-fit names (pharma/paints etc.) |
| [bhosari-midc-outreach-log.csv](bhosari-midc-outreach-log.csv) | Empty call-log template |

Rebuild from curated sources:

```bash
python scripts/build_bhosari_prospects.py
```

## Excel workbook (ready to open)

**[Bhosari_MIDC_Prospects_Bharatweld.xlsx](Bhosari_MIDC_Prospects_Bharatweld.xlsx)** — all tabs in one file (README, Prospects, Hot_List, Deferred, Parked, Lookup_Tiers, Outreach_Log).

Rebuild Excel after regenerating CSVs:

```bash
python scripts/build_bhosari_prospects.py
python scripts/export_bhosari_excel.py
```

## Import to Google Sheets (optional)

1. Upload `Bhosari_MIDC_Prospects_Bharatweld.xlsx` to Google Drive → Open with Google Sheets, **or**
2. Create a spreadsheet and import each CSV into its own tab:
   - `Prospects` ← bhosari-midc-prospects.csv
   - `Hot_List` ← bhosari-midc-hot-list.csv
   - `Deferred` ← bhosari-midc-deferred.csv
   - `Parked` ← bhosari-midc-parked.csv
   - `Lookup_Tiers` ← lookup_tiers.csv
   - `Outreach_Log` ← bhosari-midc-outreach-log.csv
3. On **Prospects**, create a filter view: `priority_label = Hot` AND `outreach_status = Not contacted`.

## First-week outreach

1. Open **Hot_List** (or Hot filter on Prospects).
2. Prefer rows with `verification_status = Phone-ok` and a website (stronger data).
3. For directory-sourced rows, open `google_maps_url`, confirm the unit still exists, then call.
4. Pitch by industry (see Lookup_Tiers): fabricators/boilers → **E7018 + E6013**; sheet/gates → **E6013**; maintenance/foundry → **cutting + Mn hardfacing**.
5. Log every touch in **Outreach_Log** and set `outreach_status` on Prospects.

## Data quality notes

- Phones from older public MIDC directories may be stale — treat as **leads to verify**, not guaranteed dial lists.
- Website-sourced Tier 1 accounts (Silson, Rakhoh, Fabri-Tek, Radiant, Malgudi, etc.) are the best first calls.
- Owner/purchase names are included only when publicly listed; do not invent decision-makers.
- Re-verify numbers older than ~6 months before a bulk WhatsApp blast.

## Column groups (Prospects)

- **Identity:** company_id, name, **plant_name**, address, block, tier, industry, **products_services**, size
- **Contact:** phone, WhatsApp, email, website, contact person/role
- **Sales intel:** electrode_likely, volume_signal, pitch_angle, priority_score/label
- **CRM:** outreach_status, verification_status, notes, assigned_to

Enriched plants (examples): SNEHA (J-40), Jaisons (T-48), MILKON (T-103), Sankalp Steeltech (Sector 7), MACHINESPACE (Sector 7 Plot 76), Super-Tech (J-251/252).

## Import into Admin CRM

```bash
php scripts/import_bhosari_to_crm.php --replace-tests
```

Loads all 100 Bhosari prospects into `storage/crm.sqlite` (State=Maharashtra, District=Pune, MIDC=Bhosari MIDC). Re-run safely: same company names are updated, not duplicated.
