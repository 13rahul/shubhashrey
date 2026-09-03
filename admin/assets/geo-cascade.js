/**
 * Cascade State → District → MIDC in admin forms and filters.
 * Expects window.SHUBH_DISTRICTS_BY_STATE and window.SHUBH_MIDCS_BY_STATE_DISTRICT.
 */
(function () {
  function districtsMap() {
    return window.SHUBH_DISTRICTS_BY_STATE || {};
  }

  function midcsMap() {
    return window.SHUBH_MIDCS_BY_STATE_DISTRICT || {};
  }

  function fallbackMidcs() {
    return window.SHUBH_MIDC_FALLBACK || [
      'Other / Outside MIDC',
      'Non-MIDC Industrial Estate',
    ];
  }

  function midcsFor(state, district) {
    if (!state || state === 'all' || !district || district === 'all') {
      return fallbackMidcs().slice();
    }
    const byState = midcsMap()[state] || {};
    const list = (byState[district] || []).slice();
    fallbackMidcs().forEach((m) => {
      if (!list.includes(m)) list.push(m);
    });
    list.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
    return list;
  }

  function fillSelect(select, placeholder, values, keepValue, allowKeepExtra) {
    const prev = keepValue !== undefined ? keepValue : select.value;
    select.innerHTML = '';
    const empty = document.createElement('option');
    empty.value = placeholder.value;
    empty.textContent = placeholder.label;
    select.appendChild(empty);
    values.forEach((v) => {
      const opt = document.createElement('option');
      opt.value = v;
      opt.textContent = v;
      if (v === prev) opt.selected = true;
      select.appendChild(opt);
    });
    if (allowKeepExtra && prev && prev !== placeholder.value && !values.includes(prev)) {
      const opt = document.createElement('option');
      opt.value = prev;
      opt.textContent = prev;
      opt.selected = true;
      select.appendChild(opt);
    }
  }

  function fillDistricts(stateSelect, districtSelect, keepValue) {
    const state = stateSelect.value;
    const list = districtsMap()[state] || [];
    fillSelect(
      districtSelect,
      { value: '', label: 'Select district' },
      list,
      keepValue === undefined ? '' : keepValue,
      true
    );
  }

  function fillMidcs(stateSelect, districtSelect, midcSelect, keepValue) {
    const list = midcsFor(stateSelect.value, districtSelect.value);
    fillSelect(
      midcSelect,
      { value: '', label: 'Select MIDC' },
      list,
      keepValue === undefined ? '' : keepValue,
      true
    );
  }

  function fillFilterDistricts() {
    const stateSel = document.getElementById('state');
    const distSel = document.getElementById('district');
    if (!stateSel || !distSel) return;
    const state = stateSel.value;
    const map = districtsMap();
    const list =
      !state || state === 'all'
        ? Object.values(map)
            .flat()
            .sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }))
        : map[state] || [];
    fillSelect(distSel, { value: 'all', label: 'All districts' }, list, distSel.value, true);
  }

  function fillFilterMidcs() {
    const stateSel = document.getElementById('state');
    const distSel = document.getElementById('district');
    const midcSel = document.getElementById('midc');
    if (!stateSel || !distSel || !midcSel) return;

    const state = stateSel.value;
    const district = distSel.value;
    let list;
    if ((!state || state === 'all') && (!district || district === 'all')) {
      // All MIDCs across known map (for browsing filters only)
      const flat = [];
      Object.values(midcsMap()).forEach((byDist) => {
        Object.values(byDist).forEach((arr) => {
          arr.forEach((m) => {
            if (!flat.includes(m)) flat.push(m);
          });
        });
      });
      fallbackMidcs().forEach((m) => {
        if (!flat.includes(m)) flat.push(m);
      });
      flat.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
      list = flat;
    } else if (state && state !== 'all' && (!district || district === 'all')) {
      const byDist = midcsMap()[state] || {};
      const flat = [];
      Object.values(byDist).forEach((arr) => {
        arr.forEach((m) => {
          if (!flat.includes(m)) flat.push(m);
        });
      });
      fallbackMidcs().forEach((m) => {
        if (!flat.includes(m)) flat.push(m);
      });
      flat.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
      list = flat;
    } else {
      list = midcsFor(state === 'all' ? 'Maharashtra' : state, district);
      // If filter state is "all" but district picked, search all states for that district name
      if ((!state || state === 'all') && district && district !== 'all') {
        const flat = [];
        Object.values(midcsMap()).forEach((byDist) => {
          (byDist[district] || []).forEach((m) => {
            if (!flat.includes(m)) flat.push(m);
          });
        });
        fallbackMidcs().forEach((m) => {
          if (!flat.includes(m)) flat.push(m);
        });
        flat.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
        list = flat;
      }
    }

    fillSelect(midcSel, { value: 'all', label: 'All MIDC' }, list, midcSel.value, true);
  }

  function bindFormCascades() {
    document.querySelectorAll('[data-geo-state]').forEach((stateSel) => {
      const districtId = stateSel.getAttribute('data-district-target');
      const midcId = stateSel.getAttribute('data-midc-target');
      const districtSel = districtId ? document.getElementById(districtId) : null;
      const midcSel = midcId ? document.getElementById(midcId) : null;
      if (!districtSel) return;

      stateSel.addEventListener('change', () => {
        fillDistricts(stateSel, districtSel, '');
        if (midcSel) fillMidcs(stateSel, districtSel, midcSel, '');
      });

      if (midcSel) {
        districtSel.addEventListener('change', () => {
          fillMidcs(stateSel, districtSel, midcSel, '');
        });
      }
    });
  }

  function bindFilterCascades() {
    const filterState = document.getElementById('state');
    const filterDistrict = document.getElementById('district');
    if (!filterState) return;
    filterState.addEventListener('change', () => {
      fillFilterDistricts();
      fillFilterMidcs();
    });
    if (filterDistrict) {
      filterDistrict.addEventListener('change', fillFilterMidcs);
    }
    // Align filter MIDC options to current state/district on load
    fillFilterMidcs();
  }

  bindFormCascades();
  bindFilterCascades();
})();
