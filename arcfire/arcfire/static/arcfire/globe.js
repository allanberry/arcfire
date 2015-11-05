// Django
{% load staticfiles %}
// end Django

var width = 500,
    height = 500;

var projection = d3.geo.orthographic()
    .scale(500)
    .translate([width / 2, height / 2])
    .clipAngle(90)
    .rotate([0, -90]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height);

var graticule = d3.geo.graticule();

// var λ = d3.scale.linear()
//     .domain([0, width])
//     .range([-180, 180]);

// var φ = d3.scale.linear()
//     .domain([0, height])
//     .range([90, -90]);

// svg.on("mousemove", function() {
//   var p = d3.mouse(this);
//   projection.rotate([λ(p[0]), φ(p[1])]);
//   svg.selectAll("path").attr("d", path);
// });

var world = "{% static 'arcfire/world-50m.js' %}"

d3.json(world, function(error, world) {
  if (error) throw error;

    svg.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

    svg.append("path")
      .datum(topojson.feature(world, world.objects.land))
      .attr("class", "land")
      .attr("d", path);
});