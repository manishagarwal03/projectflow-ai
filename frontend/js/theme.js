// Theme management (dark/light mode)

function getTheme() {
  return localStorage.getItem('theme') || 'light';
}

function setTheme(theme) {
  localStorage.setItem('theme', theme);
  applyTheme(theme);
}

function applyTheme(theme) {
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.removeAttribute('data-theme');
  }
}

function toggleTheme() {
  const currentTheme = getTheme();
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  setTheme(newTheme);
  updateThemeToggleButton();
}

function updateThemeToggleButton() {
  const button = document.getElementById('theme-toggle');
  if (button) {
    const theme = getTheme();
    button.textContent = theme === 'light' ? '🌙 Dark' : '☀️ Light';
  }
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
  applyTheme(getTheme());
  updateThemeToggleButton();
});
