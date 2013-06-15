$(function(){
	/*========================================================*/
	/* Ranges
	/*========================================================*/
	$('#demo1').jrumble({
		x: 2,
		y: 2,
		rotation: 1
	});
	
	$('#demo2').jrumble({
		x: 10,
		y: 10,
		rotation: 4
	});
	
	$('#demo3').jrumble({
		x: 4,
		y: 0,
		rotation: 0
	});
	
	$('#demo4').jrumble({
		x: 0,
		y: 0,
		rotation: 5
	});
	
	$('#demo1, #demo2, #demo3, #demo4').hover(function(){
		$(this).trigger('startRumble');
	}, function(){
		$(this).trigger('stopRumble');
	});
	
	/*========================================================*/
	/* Speeds
	/*========================================================*/
	$('#demo5').jrumble({
		speed: 0
	});
	
	$('#demo6').jrumble({
		speed: 50
	});
	
	$('#demo7').jrumble({
		speed: 100
	});
	
	$('#demo8').jrumble({
		speed: 200
	});
	
	$('#demo5, #demo6, #demo7, #demo8').hover(function(){
		$(this).trigger('startRumble');
	}, function(){
		$(this).trigger('stopRumble');
	});
	
	/*========================================================*/
	/* Opacity
	/*========================================================*/
	$('#demo9').jrumble({
		opacity: true
	});
	
	$('#demo10').jrumble({
		opacity: true,
		opacityMin: .75
	});
	
	$('#demo11').jrumble({
		opacity: true,
		opacityMin: .1
	});
	
	$('#demo12').jrumble({
		x: 6,
		y: 6,
		rotation: 6,
		speed: 5,
		opacity: true,
		opacityMin: .05
	});
	
	$('#demo9, #demo10, #demo11, #demo12').hover(function(){
		$(this).trigger('startRumble');
	}, function(){
		$(this).trigger('stopRumble');
	});
	
	/*========================================================*/
	/* Trigger Examples
	/*========================================================*/
	$('#demo13, #demo14, #demo15, #demo16, #demo17, #demo18, #demo19, #demo20').jrumble();
	
	$('#demo13').hover(function(){
		$(this).trigger('startRumble');
	}, function(){
		$(this).trigger('stopRumble');
	});
	
	$('#demo14').toggle(function(){
		$(this).trigger('startRumble');
	}, function(){
		$(this).trigger('stopRumble');
	});
	
	$('#demo15').bind({
		'mousedown': function(){
			$(this).trigger('startRumble');
		},
		'mouseup': function(){
			$(this).trigger('stopRumble');
		}
	});
	
	$('#demo16').trigger('startRumble');
	
	$('#demo17').hover(function(){
		$('#demo18').trigger('startRumble');
	}, function(){
		$('#demo18').trigger('stopRumble');
	});
	
	$('#demo18').hover(function(){
		$('#demo17').trigger('startRumble');
	}, function(){
		$('#demo17').trigger('stopRumble');
	});
	
	var demoTimeout;
	$('#demo19').click(function(){
		$this = $(this);
		clearTimeout(demoTimeout);
		$this.trigger('startRumble');
		demoTimeout = setTimeout(function(){$this.trigger('stopRumble');}, 1500)
	});
	
	var demoStart = function(){
		$('#demo20').trigger('startRumble');
		setTimeout(demoStop, 300);
	};
	
	var demoStop = function(){
		$('#demo20').trigger('stopRumble');
		setTimeout(demoStart, 300);
	};
	
	demoStart();		
	
	/*========================================================*/
	/* Source Toggling
	/*========================================================*/
	$('.view-source pre').hide();
	$('.view-source a').toggle(function(){
	$(this).css({'background': '#ddd', 'color': '#666', 'text-shadow': '1px 1px 0 #eee'}).siblings('pre').stop(false, true).slideDown(500);
	$(this).html('Hide Source');
	}, function(){
	$(this).css({'background': '#bbb','color': '#fff', 'text-shadow': '-1px 1px 0px rgba(0,0,0,.2)'}).siblings('pre').stop(false, true).slideUp(500);
	$(this).html('View Source');
	});
});