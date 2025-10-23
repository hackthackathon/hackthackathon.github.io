/* marquee.js
   Dynamically measures marquee width and sets CSS animation distance/duration
   to ensure smooth, gap-free scrolling in all browsers (including Safari).
*/

(function () {
  var SPEED = 200;

  function setupMarquee(root) {
    var track = root.querySelector('.marquee__inner');
    if (!track) return;

    var kids = Array.prototype.slice.call(track.children);
    if (kids.length < 2) return;

    var half = Math.floor(kids.length / 2);

    var r0 = kids[0].getBoundingClientRect();
    var rH = kids[half].getBoundingClientRect();
    var distance = Math.round(rH.left - r0.left);

    if (!(distance > 0)) {
      distance = 0;
      for (var i = 0; i < half; i++) {
        var el = kids[i];
        var cs = getComputedStyle(el);
        distance += el.offsetWidth + parseFloat(cs.marginRight || 0);
      }
      distance = Math.round(distance);
    }

    var dur = (distance / SPEED).toFixed(3) + 's';

    track.style.setProperty('--w', distance + 'px');
    track.style.setProperty('--dur', dur);
  }

  function initAll() {
    var marquees = document.querySelectorAll('.image-marquee');
    Array.prototype.forEach.call(marquees, setupMarquee);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  window.addEventListener('resize', initAll);
})();