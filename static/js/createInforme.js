
$('#departamentos').on('change',function(){
	
    $($(this).find('option:selected').attr('id')).show();
});
