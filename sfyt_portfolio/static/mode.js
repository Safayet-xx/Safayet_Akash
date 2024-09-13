document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
  
    // Check the current theme from local storage or default to light
    const currentTheme = localStorage.getItem('theme') || 'light-theme';
    document.body.classList.add(currentTheme);
  
    // Update the icon based on the current theme
    updateIcon(currentTheme);
  
    toggleButton.addEventListener('click', () => {
      if (document.body.classList.contains('light-theme')) {
        document.body.classList.replace('light-theme', 'dark-theme');
        localStorage.setItem('theme', 'dark-theme');
        updateIcon('dark-theme');
      } else {
        document.body.classList.replace('dark-theme', 'light-theme');
        localStorage.setItem('theme', 'light-theme');
        updateIcon('light-theme');
      }
    });
  
    function updateIcon(theme) {
      themeIcon.textContent = theme === 'light-theme' ? '🌞' : '🌜'; // Sun for light, Moon for dark
    }
  });
  