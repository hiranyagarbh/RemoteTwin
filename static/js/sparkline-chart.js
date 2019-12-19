var Script = function () {

	$(".sparkline").each(function () {
		var $data = $(this).data();

		$data.valueSpots = {
			'0:': $data.spotColor
		};

		$(this).sparkline($data.data || "html", $data, {
			tooltipFormat: '<span style="display:block; padding:0px 10px 12px 0px;">' +
				'<span style="color: {{color}}">&#9679;</span> {{offset:names}} ({{percent.1}}%)</span>'
		});
	});
}();