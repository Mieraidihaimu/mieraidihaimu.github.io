/* Content and disclosures work without JavaScript. This only manages the theme. */
(function () {
  'use strict';
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle-btn');
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  let savedTheme;
  try {
    savedTheme = localStorage.getItem('mier_theme');
  } catch (_) {
    // Storage may be unavailable in private browsing or a local file preview.
  }
  if (savedTheme !== 'dark' && savedTheme !== 'light') savedTheme = null;
  function applyTheme(theme) {
    root.dataset.theme = theme;
    button.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`);
  }
  if (!button) return;
  applyTheme(savedTheme || (preference.matches ? 'dark' : 'light'));
  button.hidden = false;
  button.addEventListener('click', () => {
    savedTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(savedTheme);
    try {
      localStorage.setItem('mier_theme', savedTheme);
    } catch (_) {
      // Keep the toggle usable even when preferences cannot be persisted.
    }
  });
  preference.addEventListener('change', (event) => {
    if (!savedTheme) applyTheme(event.matches ? 'dark' : 'light');
  });
})();
