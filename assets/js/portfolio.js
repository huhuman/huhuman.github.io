/* Local progressive enhancement. All portfolio content is readable without JS. */
(() => {
  "use strict";
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  let storedTheme = null;
  try {
    storedTheme = localStorage.getItem("portfolio-theme");
  } catch (_) {
    /* Storage may be disabled. */
  }
  let explicitTheme = storedTheme === "dark" || storedTheme === "light" ? storedTheme : null;
  const setTheme = () => {
    const dark = explicitTheme ? explicitTheme === "dark" : preference.matches;
    document.documentElement.dataset.theme = dark ? "dark" : "light";
    const button = document.querySelector(".theme-toggle");
    if (button) button.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  };
  setTheme();
  preference.addEventListener("change", setTheme);
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme-toggle");
    if (button) {
      button.hidden = false;
      button.addEventListener("click", () => {
        explicitTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        try {
          localStorage.setItem("portfolio-theme", explicitTheme);
        } catch (_) {
          /* Optional preference. */
        }
        setTheme();
      });
      setTheme();
    }
    const input = document.getElementById("publication-query");
    if (input) {
      const entries = Array.from(document.querySelectorAll(".publications li")).filter((item) => item.querySelector(".publication-entry"));
      const count = document.getElementById("publication-count");
      document.querySelector(".publication-filter").hidden = false;
      const filter = () => {
        const query = input.value.trim().toLocaleLowerCase();
        let visible = 0;
        entries.forEach((entry) => {
          entry.hidden = !entry.textContent.toLocaleLowerCase().includes(query);
          if (!entry.hidden) visible += 1;
        });
        document.querySelectorAll(".publications h2.bibliography").forEach((heading) => {
          const list = heading.nextElementSibling;
          heading.hidden = list ? !Array.from(list.children).some((item) => !item.hidden) : false;
        });
        count.textContent = visible === 1 ? "1 publication" : visible + " publications";
      };
      input.addEventListener("input", filter);
      filter();
    }
  });
})();
