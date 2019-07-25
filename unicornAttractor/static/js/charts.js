queue()
    .defer(d3.json, 'get_data')
    .await(makeGraphs);

function makeGraphs(error, jsonTickets){
    
    var graphData = []  

    jsonTickets.forEach(function(ticket){
        graphData.push(ticket['fields']);
    });

    var formatTime = d3.time.format("%Y-%m-%d");

    graphData.forEach(function(d){
        var formattedDate = formatTime(new Date(d.lastUpdatedDateTime));
        var tempDate = new Date(formattedDate + 'T00:00:00');
        d.lastUpdatedDateTime = tempDate;
    })
    
    
    endDate = graphData[0].lastUpdatedDateTime;
    startDate = graphData[graphData.length-1].lastUpdatedDateTime;

    function makeDateArray(start, end){
        
        var returnArray = []
        var tempDate = new Date(start)

        while (tempDate <= end){
            returnArray.push({ date: new Date(tempDate), amount: 0});
            tempDate.setDate(tempDate.getDate()+1);
        }
        return returnArray
    }

    dateRange = makeDateArray(startDate, endDate);
    
    graphData.forEach(function(d){
        tempDate = d.lastUpdatedDateTime.toString();
        dateRange.forEach(function(dr){
            tempDr = dr.date.toString();
            if (tempDate == tempDr){
                dr.amount += 1;
            }
        });
    });

    var ndx = crossfilter(dateRange);

    closedChart(ndx);
    closedChartMobile(ndx);
    
    dc.renderAll();
}   

function closedChart(ndx){
    
    var dim = ndx.dimension(dc.pluck('date'));
    var group = dim.group().reduceSum(function(d){ return d.amount });

    var minDate = dim.bottom(1)[0].date;
    var maxDate = dim.top(1)[0].date;

    dc.lineChart('#closed-chart')
        .width($('#closed-chart').parent().width())
        .height(400)
        .margins({top:20, bottom:50, right:20, left:40})
        .x(d3.time.scale().domain([minDate, maxDate]))
        .y(d3.scale.linear().domain([0, 5]))
        .brushOn(false)
        .xAxisLabel("Date")
        .yAxisLabel("Closed")
        .clipPadding(10)
        .dimension(dim)
        .group(group)
        .renderArea(true)
        .yAxis().ticks(5);
}

function closedChartMobile(ndx){
    
    var dim = ndx.dimension(dc.pluck('date'));
    var group = dim.group().reduceSum(function(d){ return d.amount });

    var minDate = dim.bottom(1)[0].date;
    var maxDate = dim.top(1)[0].date;

    dc.lineChart('#closed-chart-mobile')
        .width($('#closed-chart-mobile').parent().width())
        .height(200)
        .margins({top:20, bottom:80, right:20, left:25})
        .x(d3.time.scale().domain([minDate, maxDate]))
        .y(d3.scale.linear().domain([0, 5]))
        .brushOn(false)
        .xAxisLabel("Date")
        .yAxisLabel("Closed")
        .clipPadding(10)
        .dimension(dim)
        .group(group)
        .renderArea(true)
        .yAxis().ticks(5);
}