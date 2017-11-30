/* Javascript for TableCreaterXBlock. */
function TableCreaterXBlock(runtime, element) {

    $(element).find('.action-cancel').bind('click',function(){
        runtime.notify('cancel',{});
    });

    var handlerUrl = runtime.handlerUrl(element,'save_tablecreater');

    $(element).find('.action-save').bind('click',function(){
        var data = {
            'csv_url':('#tablecreater_edit_csv_url').val()
        };

        console.log(data);

        runtime.notify('save',{state:'start'});

        $.post(handlerUrl, JSON.stringify(data)).done(function (response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}
