!(function () {
  "use strict";
  let e = document.querySelector(".header-nav");
  var n = 0,
    t = 0;
  const s = { pinned: "header-nav-pinned", unpinned: "header-nav-unpinned" };
  function c() {
    50 <= window.scrollY
      ? e.classList.add("header-sticky-top")
      : e.classList.remove("header-sticky-top");
  }
  function i() {
    (t = window.pageYOffset) < n
      ? e.classList.contains(s.unpinned) &&
        (e.classList.remove(s.unpinned), e.classList.add(s.pinned))
      : n < t &&
        400 <= window.scrollY &&
        ((!e.classList.contains(s.pinned) &&
          e.classList.contains(s.unpinned)) ||
          (e.classList.remove(s.pinned), e.classList.add(s.unpinned))),
      (n = t);
  }
  (window.onload = function () {
    window.onscroll = function () {
      i(), c();
    };
  }),
    window.addEventListener(
      "load",
      function () {
        Lightense(".content img"),
          (window.onscroll = function () {
            i(), c();
          });
      },
      !1
    ),
    (function () {
      let n = document.querySelector(".search-block"),
        e = document.querySelectorAll('[data-toggle="search"]'),
        t = document.querySelector('[data-toggle="search-close"]');
      e.forEach((e) => {
        e.addEventListener("click", function () {
          n.classList.add("is-visible"),
            setTimeout(() => {
              document.querySelector('[aria-label="search-query"]').focus();
            }, 250);
        });
      }),
        t.addEventListener("click", function () {
          n.classList.remove("is-visible"),
            (document.querySelector('[aria-label="search-query"]').value = ""),
            setTimeout(() => {
              (document.querySelector(
                "#js-search-results-container"
              ).innerHTML = ""),
                (document.querySelector(
                  "#js-search-results-container"
                ).style.display = "none");
            }, 250);
        });
    })(),
    document
      .querySelector(".navbar-toggler")
      .addEventListener("click", function (e) {
        this.classList.toggle("toggle-menu");
      });
})();