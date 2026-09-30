/* Mahajan Dental Care — site interactions */
(function(){
  "use strict";

  document.addEventListener("DOMContentLoaded", function(){

    var header = document.querySelector(".site-header");
    if(header){
      var onScroll = function(){ header.classList.toggle("scrolled", window.scrollY > 8); };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive:true });
    }

    var toggle = document.querySelector("[data-nav-toggle]");
    var drawer = document.querySelector("[data-mobile-nav]");
    var scrim = document.querySelector("[data-nav-scrim]");
    var closeBtn = document.querySelector("[data-nav-close]");
    function setNav(open){
      if(drawer) drawer.classList.toggle("open", open);
      if(scrim) scrim.classList.toggle("show", open);
      if(toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    }
    if(toggle) toggle.addEventListener("click", function(){ setNav(!drawer.classList.contains("open")); });
    if(closeBtn) closeBtn.addEventListener("click", function(){ setNav(false); });
    if(scrim) scrim.addEventListener("click", function(){ setNav(false); });
    document.querySelectorAll(".mobile-nav a").forEach(function(a){ a.addEventListener("click", function(){ setNav(false); }); });

    var reveals = document.querySelectorAll("[data-reveal]");
    if("IntersectionObserver" in window && reveals.length){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }
        });
      }, { threshold:.1, rootMargin:"0px 0px -6% 0px" });
      reveals.forEach(function(el){ io.observe(el); });
    } else {
      reveals.forEach(function(el){ el.classList.add("in"); });
    }

    var slideshow = document.querySelector("[data-hero-slideshow]");
    if(slideshow){
      var slides = slideshow.querySelectorAll(".hero__slide");
      var dotsWrap = document.querySelector("[data-hero-dots]");
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if(slides.length > 1){
        var i = 0, timer = null, DELAY = 4800;
        var dots = [];
        if(dotsWrap){
          slides.forEach(function(_, idx){
            var b = document.createElement("button");
            b.type = "button";
            b.setAttribute("aria-label", "Slide " + (idx+1));
            if(idx === 0) b.classList.add("is-active");
            b.addEventListener("click", function(){ go(idx); reset(); });
            dotsWrap.appendChild(b);
            dots.push(b);
          });
        }
        var go = function(n){
          slides[i].classList.remove("is-active");
          if(dots[i]) dots[i].classList.remove("is-active");
          i = (n + slides.length) % slides.length;
          slides[i].classList.add("is-active");
          if(dots[i]) dots[i].classList.add("is-active");
        };
        var next = function(){ go(i+1); };
        var start = function(){ if(!reduce){ timer = setInterval(next, DELAY); } };
        var reset = function(){ clearInterval(timer); start(); };
        start();
        document.addEventListener("visibilitychange", function(){
          if(document.hidden){ clearInterval(timer); } else { start(); }
        });
      }
    }

    document.querySelectorAll("form[data-wa-form]").forEach(function(f){
      f.addEventListener("submit", function(e){
        e.preventDefault();
        var name = (f.querySelector('[name="name"]') || {}).value || "";
        var msg = (f.querySelector('[name="message"]') || {}).value || "";
        var text = "Hello Mahajan Dental Care, my name is " + name + ". " + msg;
        var url = "https://wa.me/919873140343?text=" + encodeURIComponent(text.trim());
        window.open(url, "_blank", "noopener");
        var note = f.querySelector(".form__msg");
        if(note){ note.classList.add("ok"); note.textContent = "Opening WhatsApp so you can send this straight to our team."; }
      });
    });

  });
})();
