(function() {
  var script = document.getElementById('google-analytics-script');
  if (script) {
    var gid = script.getAttribute('data-gid');
    if (gid) {
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag('js', new Date());
      gtag('config', gid);
    }
  }
})();
