/* Javascript for TableCreaterXBlock. */
function TableCreaterXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    getHtml(runtime,element);


    function getHtml(runtime,element){
        $.ajax({
            type: "POST",
            url: runtime.handlerUrl(element,'getHtml'),
            data: JSON.stringify({"hello":"hi"}),
            success: function(result){
                console.log(result);
            },
            error:function(){
                console.log("error");
            }
        });
    }
}
