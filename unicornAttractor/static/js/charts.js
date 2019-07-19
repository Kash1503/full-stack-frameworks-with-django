queue()
    .defer(d3.json, 'get_data')
    .await(makeGraphs);

function makeGraphs(error, graphData){

    var ndx = crossfilter(graphData);

    statusChart(ndx);
    
    dc.renderAll();
}   

function statusChart(ndx){
    
    var dim = ndx.dimension(dc.pluck('ticket_type'));
    var group = dim.group();
    
    dc.pieChart('#status-chart')
        .width(500)
        .height(350)
        .dimension(dim)
        .group(group)
        .transitionDuration(500)
        .legend(dc.legend().x(400).y(50).itemHeight(10).gap(5))
        .externalRadiusPadding(50)
        .minAngleForLabel(361);
}
    