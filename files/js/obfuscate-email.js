document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.obfuscated-email').forEach(function(link){
    var user = 'contact';
    var domain = 'hackthehackathon';
    var tld = 'org';
    var email = user + '@' + domain + '.' + tld;

    link.href = 'mailto:' + email;
    link.title = email;
    if (!link.getAttribute('aria-label')) link.setAttribute('aria-label', 'Email ' + user);
  });
});