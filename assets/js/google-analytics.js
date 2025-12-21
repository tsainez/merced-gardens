(function() {
  var script = document.currentScript;
  // Fallback for older browsers or if currentScript is not available (though unlikely in modern context)
  if (!script) {
    script = document.querySelector('script[data-gid]');
  }

  if (script) {
    var gid = script.getAttribute('data-gid');
    if (gid) {
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      window.gtag = gtag; // Expose globally as per standard GA setup

      gtag('js', new Date());
      gtag('config', gid);
    }
  }
})();
