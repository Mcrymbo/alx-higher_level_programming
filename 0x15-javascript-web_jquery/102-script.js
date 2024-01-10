$('document').ready(function() {
	const url = 'https://www.fourtonfish.com/hellosalut/hello/;
	const lan = $('INPUT#language_code').val();
	$('INPUT#btn_translate').on('click', function () {
		$.get(url, { lang: lan }, function (data) {
			$('DIV#hello').text(data.hello);
		});
	});
})
