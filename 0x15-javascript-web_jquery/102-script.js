const $ = window.$;
$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('input#btn_translate').on('click', function () {
    const lan = $('input#language_code').val();
    $.get(url, { lang: lan }, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
