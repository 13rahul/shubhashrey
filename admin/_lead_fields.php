<?php
declare(strict_types=1);

/**
 * Shared editable fields for Add / Edit lead forms.
 *
 * @param array<string, mixed> $lead
 * @param list<string> $statuses
 * @param list<string> $sources
 * @param list<string> $stateOptions
 * @param list<string> $midcOptions unused when districtsByState is provided (kept for call-site compat)
 * @param array<string, list<string>> $districtsByState
 */
function render_lead_fields(
    array $lead,
    array $statuses,
    array $sources,
    array $stateOptions,
    array $midcOptions,
    string $prefix = 'f',
    array $districtsByState = []
): void {
    $pid = preg_replace('/[^a-z0-9_-]/i', '', $prefix) ?: 'f';
    $v = static function (string $key) use ($lead): string {
        return shubh_h((string) ($lead[$key] ?? ''));
    };
    $currentState = (string) ($lead['state'] ?? '');
    $currentDistrict = (string) ($lead['district'] ?? '');
    $currentMidc = (string) ($lead['midc'] ?? '');

    $districtChoices = $districtsByState[$currentState] ?? [];
    if ($currentDistrict !== '' && !in_array($currentDistrict, $districtChoices, true)) {
        $districtChoices[] = $currentDistrict;
        natcasesort($districtChoices);
        $districtChoices = array_values($districtChoices);
    }

    $midcChoices = function_exists('shubh_midcs_for')
        ? shubh_midcs_for($currentState, $currentDistrict)
        : $midcOptions;
    if ($currentMidc !== '' && !in_array($currentMidc, $midcChoices, true)) {
        $midcChoices[] = $currentMidc;
        natcasesort($midcChoices);
        $midcChoices = array_values($midcChoices);
    }
    ?>
    <div class="field">
      <label for="<?= $pid ?>_name">Name *</label>
      <input id="<?= $pid ?>_name" name="name" required value="<?= $v('name') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_company">Company</label>
      <input id="<?= $pid ?>_company" name="company" value="<?= $v('company') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_phone">Phone</label>
      <input id="<?= $pid ?>_phone" name="phone" value="<?= $v('phone') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_email">Email</label>
      <input id="<?= $pid ?>_email" name="email" type="email" value="<?= $v('email') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_status">Status</label>
      <select id="<?= $pid ?>_status" name="status">
        <?php foreach ($statuses as $st): ?>
          <option value="<?= shubh_h($st) ?>" <?= ($lead['status'] ?? '') === $st ? 'selected' : '' ?>><?= shubh_h(ucfirst($st)) ?></option>
        <?php endforeach; ?>
      </select>
    </div>
    <div class="field">
      <label for="<?= $pid ?>_source">Source</label>
      <select id="<?= $pid ?>_source" name="source">
        <?php foreach ($sources as $src): ?>
          <option value="<?= shubh_h($src) ?>" <?= ($lead['source'] ?? '') === $src ? 'selected' : '' ?>><?= shubh_h($src) ?></option>
        <?php endforeach; ?>
      </select>
    </div>
    <div class="field">
      <label for="<?= $pid ?>_city">City</label>
      <input id="<?= $pid ?>_city" name="city" value="<?= $v('city') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_state">State</label>
      <select
        id="<?= $pid ?>_state"
        name="state"
        data-geo-state
        data-district-target="<?= $pid ?>_district"
        data-midc-target="<?= $pid ?>_midc"
      >
        <option value="">Select state</option>
        <?php foreach ($stateOptions as $st): ?>
          <option value="<?= shubh_h($st) ?>" <?= $currentState === $st ? 'selected' : '' ?>><?= shubh_h($st) ?></option>
        <?php endforeach; ?>
      </select>
    </div>
    <div class="field">
      <label for="<?= $pid ?>_district">District</label>
      <select id="<?= $pid ?>_district" name="district" data-geo-district>
        <option value="">Select district</option>
        <?php foreach ($districtChoices as $d): ?>
          <option value="<?= shubh_h($d) ?>" <?= $currentDistrict === $d ? 'selected' : '' ?>><?= shubh_h($d) ?></option>
        <?php endforeach; ?>
      </select>
    </div>
    <div class="field">
      <label for="<?= $pid ?>_midc">MIDC</label>
      <select id="<?= $pid ?>_midc" name="midc" data-geo-midc>
        <option value="">Select MIDC</option>
        <?php foreach ($midcChoices as $m): ?>
          <option value="<?= shubh_h($m) ?>" <?= $currentMidc === $m ? 'selected' : '' ?>><?= shubh_h($m) ?></option>
        <?php endforeach; ?>
      </select>
      <p class="muted" style="margin:.35rem 0 0;font-size:.8rem">Options follow selected state &amp; district</p>
    </div>
    <div class="field">
      <label for="<?= $pid ?>_territory">Territory / area</label>
      <input id="<?= $pid ?>_territory" name="territory" value="<?= $v('territory') ?>" />
    </div>
    <div class="field">
      <label for="<?= $pid ?>_business_type">Business type</label>
      <input id="<?= $pid ?>_business_type" name="business_type" value="<?= $v('business_type') ?>" />
    </div>
    <div class="field field--full">
      <label for="<?= $pid ?>_interest">Interest / electrode need</label>
      <input id="<?= $pid ?>_interest" name="interest" value="<?= $v('interest') ?>" placeholder="E6013, E7018, distributor…" />
    </div>
    <div class="field field--full">
      <label for="<?= $pid ?>_message">Message / enquiry</label>
      <textarea id="<?= $pid ?>_message" name="message" rows="3"><?= $v('message') ?></textarea>
    </div>
    <div class="field field--full">
      <label for="<?= $pid ?>_notes">Notes (full)</label>
      <textarea id="<?= $pid ?>_notes" name="notes" rows="4" placeholder="Full notes history — or use + Note to append"><?= $v('notes') ?></textarea>
    </div>
    <?php
}
