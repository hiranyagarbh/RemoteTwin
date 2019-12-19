var Script = function () {
	$(function () {
		Morris.Donut({
			element: 'community_data',
			data: [
				{
					label: 'Asthama',
					value: 34
				},
				{
					label: 'COPD',
					value: 25
				},
				{
					label: 'Cystic fibrosis',
					value: 25
				},
				{
					label: 'Sugar',
					value: 10
				}
        ],
			colors: ['#139df9', '#f95c13', '#f91336'],
			formatter: function (y) {
				return y + "%"
			}
		});
	});
}();
