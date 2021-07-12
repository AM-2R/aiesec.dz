$(document).ready(function() {
  $("#slider").slider({
    value: 2002,
    min: 2002,
    max: 2018,
    step: 1,
    slide: function(event, ui) {
      $("#year").val(ui.value);
      redraw(ui.value.toString());
    }
  });
  $("#year").val($("#slider").slider("value"));

  var w = 1200;
  var h = 500;

  var xy = d3.geo.equirectangular().scale(1000);

  var path = d3.geo.path().projection(xy);

  var svg = d3
    .select("#graph")
    .insert("svg:svg")
    .attr("width", w)
    .attr("height", h);

  var states = svg.append("svg:g").attr("id", "states");

  var circles = svg.append("svg:g").attr("id", "circles");

  var labels = svg.append("svg:g").attr("id", "labels");

  d3.json("https://raw.githubusercontent.com/siboy/dev/master/data/world-countries.json", function(collection) {
    states
      .selectAll("path")
      .data(collection.features)
      .enter()
      .append("svg:path")
      .attr("d", path)
      .on("mouseover", function(d) {
        d3
          .select(this)
          .style("fill", "#6C0")
          .append("svg:title")
          .text(d.properties.name);
      })
      .on("mouseout", function(d) {
        d3.select(this).style("fill", "#ccc");
      });
  });

  //http://stackoverflow.com/questions/11386150/lat-lon-positon-on-a-d3-js-map
  // +convert to string to number

  var scalefactor = 1 / 300;

  d3.csv("https://raw.githubusercontent.com/siboy/dev/master/data/produksiminyak.csv", function(csv) {
    circles
      .selectAll("circle")
      .data(csv)
      .enter()
      .append("svg:circle")
      .attr("cx", function(d, i) {
        return xy([+d["longitude"], +d["latitude"]])[0];
      })
      .attr("cy", function(d, i) {
        return xy([+d["longitude"], +d["latitude"]])[1];
      })
      .attr("r", function(d) {
        return +d["2002"] * scalefactor;
      })
      .attr("title", function(d) {
        return d["country"] + ": " + Math.round(d["2002"]);
      })
      .on("mouseover", function(d) {
        d3.select(this).style("fill", "#FC0");
      })
      .on("mouseout", function(d) {
        d3.select(this).style("fill", "steelblue");
      });

    circles
      .selectAll("circle")
      .data(csv)
      .enter()
      .append("svg:circle")
      .attr("cx", function(d, i) {
        return xy([+d["longitude"], +d["latitude"]])[0];
      })
      .attr("cy", function(d, i) {
        return xy([+d["longitude"], +d["latitude"]])[1];
      })
      .attr("fill", "red")
      .attr("r", 15)
      .on("mouseover", function(d, i) {
        d3
          .select(this)
          .append("text")
          .text(d.x)
          .attr("x", x(d.x))
          .attr("y", y(d.y));
      });
  });

  function redraw(year) {
    circles
      .selectAll("circle")
      .transition()
      .duration(1000)
      .ease("linear")
      .attr("r", function(d) {
        return +d[year] * scalefactor;
      })
      .attr("title", function(d) {
        return d["country"] + ": " + Math.round(d[year]);
      });

    labels.selectAll("text").text(function(d) {
      return Math.round(d[year]);
    });
  }
});