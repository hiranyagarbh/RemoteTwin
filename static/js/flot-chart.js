var Script = function () {


	//    live chart

	$(function () {
		// we use an inline data source in the example, usually data would
		// be fetched from a server
		var data = [],
			totalPoints = 300;

		function getRandomData() {
			if (data.length > 0)
				data = data.slice(1);

			// do a random walk
			while (data.length < totalPoints) {
				var prev = data.length > 0 ? data[data.length - 1] : 50;
				var y = prev + Math.random() * 10 - 5;
				if (y < 0)
					y = 0;
				if (y > 100)
					y = 100;
				data.push(y);
			}

			// zip the generated y values with the x values
			var res = [];
			for (var i = 0; i < data.length; ++i)
				res.push([i, data[i]])
			return res;
		}

		// setup control widget
		var updateInterval = 30;
		$("#updateInterval").val(updateInterval).change(function () {
			var v = $(this).val();
			if (v && !isNaN(+v)) {
				updateInterval = +v;
				if (updateInterval < 1)
					updateInterval = 1;
				if (updateInterval > 2000)
					updateInterval = 2000;
				$(this).val("" + updateInterval);
			}
		});

		// setup plot
		var options = {
			series: {
				shadowSize: 0
			}, // drawing is faster without shadows
			yaxis: {
				min: 0,
				max: 100
			},
			xaxis: {
				show: false
			}
		};
		var plot = $.plot($("#ecg"), [getRandomData()], options);

		function update() {
			plot.setData([getRandomData()]);
			// since the axes don't change, we don't need to call plot.setupGrid()
			plot.draw();

			setTimeout(update, updateInterval);
		}

		update();
	});

}();
