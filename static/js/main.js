$(document).ready(function(){

	// menu

	if ($(window).width() >= 1170) { 
		$('.main-navigation > li')
		.mouseenter(function() {
			$(this).children('.submenu').addClass('submenu-show')
		})
		.mouseleave(function() {
			$(this).children('.submenu').removeClass('submenu-show')
		})

		$('.submenu').each(function(e){
			var submenu_len = $(this).children('li').length
			if (submenu_len >= 4) {
				var delimeter = Math.ceil(submenu_len / 2)

				var a = $(this).children('li').slice(0,delimeter).clone()
				$(this).children('li').slice(0,delimeter).remove()

				var b = $(this).children('li').clone()
				$(this).children('li').remove()

				$(this).append('<div class="submenu-left"></div>')
				$(this).children('.submenu-left').append(a)

				$(this).append('<div class="submenu-right"></div>')
				$(this).children('.submenu-right').append(b)

				$(this).addClass('big-submenu clearfix')
			}
		})

		var menu_top = $('.menu-wrapper').offset().top
		var menu_height = $('.menu-wrapper').height()
		$(window).scroll(function(){
			if ($(window).scrollTop() > menu_top) {
				$('.menu-wrapper').addClass('menu-stick')
				$('body').css({'margin-top': menu_height+'px'})
			} else {
				$('.menu-wrapper').removeClass('menu-stick')
				$('body').css({'margin-top': 0})
			}
		})



	} else {
		$('.lvl1 > a').click(function(e){
			e.preventDefault()
			$(this).siblings('.submenu').slideToggle()
		})
		$('.lvl2 > a').click(function(e){
			e.preventDefault()
			$(this).siblings('.submenu-lvl2').slideToggle()
		})
		$('.menu-close').click(function(){
			$('.main-navigation-wrap').fadeOut(300)
		})
		$('.mobile-menu').click(function(){
			$('.main-navigation-wrap').fadeIn(300)
		})

		$(".block3__flex").addClass('owl-carousel')
		$(".block3__flex").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$(".block4__block").addClass('owl-carousel')
		$(".block4__block").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$(".block10__flex").addClass('owl-carousel')
		$(".block10__flex").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$(".block10__flex").addClass('owl-carousel')
		$(".block10__flex").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$(".about__block2__flex").addClass('owl-carousel')
		$(".about__block2__flex").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$(".case__flex").addClass('owl-carousel')
		$(".case__flex").owlCarousel({
			items : 1,
			mouseDrag: true,
			nav: true,
			navText : ["<div class='prev-m'><img src='/static/img/left.png' /></div>", "<div class='next-m'><img src='/static/img/right.png' /></div>"],
		});

		$('.f-mobile').click(function(){
			$(this).siblings('ul').slideToggle()
		})


		//sticky menu

		var menu_top = $('.head-mobile').offset().top
		var menu_height = $('.head-mobile').height()
		$(window).scroll(function(){
			if ($(window).scrollTop() > menu_top) {
				$('.head-mobile').addClass('menu-stick')
				$('body').css({'margin-top': menu_height+'px'})
			} else {
				$('.head-mobile').removeClass('menu-stick')
				$('body').css({'margin-top': 0})
			}
		})

		//sticky menu
	}

	//menu ^

	$('.main-slider').owlCarousel({
		items : 1,
		mouseDrag: true,
		dots: true,
		lazyLoad: true,
		loop: true,
		autoplay: true,
		autoplayTimeout:5000,
		autoplayHoverPause:true,
		nav: true,
		navText : ["<div class='main-prev'><img src='/static/img/left.png' /></div>", "<div class='main-next'><img src='/static/img/right.png' /></div>"],
	});

	//block2 slider

	$('.block2__slide').each(function(e){
		$(this).attr('data-block2', e)
	})
	$('.block2__item').each(function(e){
		$(this).attr('data-block2', e)
	})
	$('.block2__slider').owlCarousel({
		items: 1,
		mouseDrag: false,
		nav: true,
		navText: ["<div class='block2-prev'><img src='/static/img/left2.png' /></div>", "<div class='block2-next'><img src='/static/img/right2.png' /></div>"],
	})
	$('.block2__slider').on('translated.owl.carousel', function(e) {
		var i = $('.block2__slider .owl-item.active .block2__slide').data('block2')
		$('.block2__item').removeClass('block2__item-active')
		$('.block2__item[data-block2='+i+']').addClass('block2__item-active')
	})
	$('.block2__item').click(function() {
		var t = $(this).data('block2')
		$('.block2__slider').trigger('to.owl.carousel', t)
		$('.block2__item').removeClass('block2__item-active')
		$('.block2__item[data-block2='+t+']').addClass('block2__item-active')
	})

	//block2 slider

	// block4 slider

	$('.block4__left').owlCarousel({
		items : 1,
		mouseDrag: true,
		dots: true,
		lazyLoad: true,
		loop: true,
		nav: true,
		navText : ["<div class='block4-prev'><img src='/static/img/left3.png' /></div>", "<div class='block4-next'><img src='/static/img/right3.png' /></div>"],
	})

	// block4 slider


	//block6-calc

	$(".block6__item button").click(function(){
		var s = parseInt($(this).siblings('.input-block').children('input').val())
		var p = parseInt($(this).parents('.block6__item__bottom').siblings('.price').children('span').text())
		var price = s*p
		$(this).siblings('.price-block').children('span').text(price)
	})

	//block6-calc


	//block8 - calc

	$('.block8__calculte').click(function(){

		var repair_price = $('#repair-type option:selected').data('price')
		var square = $('#square').val()
		var repair_total = repair_price * square
		var design_price = $('input[name=design]:checked').data('price')
		var works_price = 0
		var works_term = 0
		var works = '\n'
		$('.block8__active .block8__work input[name=work]:checked').each(function(){
			works_price = works_price + $(this).data('price')
			works_term = works_term + $(this).data('term')
			works = works + $(this).siblings('label').text() + ';\n'
		})
		var total_price = repair_total + design_price + works_price

		$('.total-price span').text(total_price)
		$('input[name=works]').val(works)
		$('input[name=works]').val(works)

		var sell = 0
		if (total_price<=100000) {sell=2}
		else if (total_price<=200000 && total_price>100000) {sell=4}
		else if (total_price<=300000 && total_price>200000) {sell=5}
		else if (total_price>300000) {sell=8}

		$('.sell span').text(sell)

		var repair_term = $('#repair-type option:selected').data('term')


		var total_term = repair_term * square
		$('.total-terms .min').text(total_term-5)
		$('.total-terms .max').text(total_term+5)

		$('.block8__result').slideDown()

	});
	$("#repair-type").on('change', function() {
		$(".block8__works").removeClass("block8__active");
		$("div[data-calc='"+this.value+"']").addClass("block8__active");
	})
	$("div[data-calc='"+$("#repair-type").val()+"']").addClass("block8__active");
	//block8 - calc


	//block9 slider

	$('.block9__slider').owlCarousel({
		items : 1,
		mouseDrag: true,
		dots: true,
		lazyLoad: true,
		loop: true,
		autoplay: true,
		autoplayTimeout:5000,
		autoplayHoverPause:true,
	});

	//block9 slider


	//block11 slider

	$('.block11__slider').owlCarousel({
		items : 1,
		mouseDrag: true,
		lazyLoad: true,
		loop: true,
		nav: true,
		navText : ["<div class='block11-prev'><img src='/static/img/left2.png' /></div>", "<div class='block11-next'><img src='/static/img/right2.png' /></div>"],
	});

	//block11 slider

	//block12 slider

	$('.block12__slider').owlCarousel({
		items : 1,
		mouseDrag: true,
		lazyLoad: true,
		loop: true,
		nav: true,
		navText : ["<div class='block12-prev'><img src='/static/img/left2.png' /></div>", "<div class='block12-next'><img src='/static/img/right2.png' /></div>"],
	});

	//block12 slider


	//block13 faq
	$('.block13__head').click(function(){
		var fText = $(this).siblings('.block13__body');

		$('.block13__head').removeClass('block13__head-active')

		$('.block13__body-active').slideToggle();
		$('.block13__body').removeClass('block13__body-active');

		if (fText.is(':hidden')) {
			fText.addClass('block13__body-active');
			fText.slideToggle();
			$(this).addClass('block13__head-active')
		}
	});
	//block13 faq

	// price

	$('.price-head').click(function(e){
		$(this).siblings('.price__submenu').slideToggle()
	})

	$('.price-i').each(function(e){
		$(this).attr('data-item', e)
	})
	$('.price__block1__item').each(function(e){
		$(this).attr('data-item', e)
	})

	$('.price-i').click(function(){
		var i = $(this).data('item')

		$('.price__block1__item').removeClass('price__current-item')
		$('.price__block1__item[data-item='+i+']').addClass('price__current-item')
	})

	// price


	// all price

	$('.all__input input').on('input', function(){
		var v = $(this).val()
		var per_one = $(this).parents('td').siblings('.per-one').text()
		var total = $(this).parents('td').siblings('.total')

		total.text(v*per_one)

		var sum = 0
		$('td.total').each(function(){
			sum = sum + parseInt($(this).text())
		})
		$('.sum').text(sum+' руб')
	})

	//all price


	//popup

	$('.main__left a').click(function (e) {
		if ($(this).attr('href').length == 0) {
			e.preventDefault()
			$('.page-wrapper').addClass('soap')
			document.body.style.overflow = 'hidden'

			$('.layer').fadeIn(300)
			$('.popup').fadeIn(500)
		}
	})
	$('.price__block1__right a').click(function (e) {
		if ($(this).attr('href').length == 0) {
			e.preventDefault()
			$('.page-wrapper').addClass('soap')
			document.body.style.overflow = 'hidden'

			$('.layer').fadeIn(300)
			$('.popup').fadeIn(500)
		}
	})

	$('.about-btn, .about-btn, .block9__block button, .header__callback').click(function(e){
		e.preventDefault()
		$('.page-wrapper').addClass('soap')
		document.body.style.overflow = 'hidden'

		$('.layer').fadeIn(300)
		$('.popup').fadeIn(500)
	})

	$('.popup .close').click(function(){
		$('.popup').fadeOut(300)
		$('.layer').fadeOut(300)
		$('.thank').fadeOut(300)
		$('.page-wrapper').removeClass('soap')
		document.body.style.overflow = 'scroll'
	})

	$('.layer').click(function(e){
		if ($(this).has(e.target).length === 0) {
			$('.popup').fadeOut(300)
			$('.layer').fadeOut(300)
		$('.thank').fadeOut(300)
			$('.page-wrapper').removeClass('soap')
			document.body.style.overflow = 'scroll'
		}
	})

	//popup


	//main tabs

	$('.block5__tabs1 .block5__tab').click(function () {
		if (!$(this).is('.block5__tab1-active')) {
			var d = $(this).data('type')
			var that = $(this)
			var a = $(this).data('all')
			$.ajax({
				url: '/projects/get_content/',
				data: {'filter': d, 'type': 1, 'all': a},
				type: 'POST',
				success: function (html) {
					$('.block5__item').fadeOut(200)
					$('.block5__tabs1 .block5__tab').removeClass('block5__tab1-active')
					that.addClass('block5__tab1-active')
					$('.block5__tabs2 .block5__tab').removeClass('block5__tab2-active')
					$('.block5__tabs2 .block5__tab').first().addClass('block5__tab2-active')
					setTimeout(function () {
						$('.block5__flex').empty()
						$(html).appendTo($('.block5__flex')).fadeIn(200)
                    }, 200)
				}
            })
        }
    })

	$('.block5__tabs2 .block5__tab').click(function () {
		if (!$(this).is('.block5__tab2-active')) {
			var d = $(this).data('filter')
			var f = $('.block5__tab1-active').data('type')
			var that = $(this)
			var a = $(this).data('all')
			$.ajax({
				url: '/projects/get_content/',
				data: {'filter': d, 'type': 2, 't': f, 'all': a},
				type: 'POST',
				success: function (html) {
					$('.block5__item').fadeOut(200)
					$('.block5__tabs2 .block5__tab').removeClass('block5__tab2-active')
					that.addClass('block5__tab2-active')
					setTimeout(function () {
						$('.block5__flex').empty()
						$(html).appendTo($('.block5__flex')).fadeIn(200)
                    }, 200)
				}
            })
        }
    })

	//main tabs end




	$('form').submit(function(e) {
		e.preventDefault()

		var data = $(this).serialize()
		console.log(data);
		$.ajax({
			url: '/send_mail/',
			data: data,
			type: 'POST',
			success: function(data) {
				$('.layer').fadeIn(300)
				$('.popup').fadeOut(300)
				setTimeout(function() {
					window.location = "http://rial-remont.ru/thankpage";
				}, 300)
			},
			error: function(err) {
				console.log(err)
			}
		})

	})

	/*$(document).mouseleave(
		function(){
			// Before using localStorage or sessionStorage, check browser support
			if (typeof(Storage) != "undefined") {
				// Retrieve session name-value pair
				var modalAlreadyShown = sessionStorage.getItem("showmodal");
				// alert('modalAlreadyShown ' + modalAlreadyShown);
				if (modalAlreadyShown != "true")
				{
					$('.page-wrapper').addClass('soap');
					document.body.style.overflow = 'hidden';
			
					$('.layer').fadeIn(300);
					$('.readfeedback').fadeIn(500);
					// Store session name-value pair
					sessionStorage.setItem("showmodal", "true");
				} // end if	
			} // end if		
		} // end anonymous function
	); // end mouseleave
*/
	$('.readfeedback .close').click(function(){
		$('.readfeedback').fadeOut(300)
		$('.layer').fadeOut(300)
		$('.page-wrapper').removeClass('soap')
		document.body.style.overflow = 'scroll'
	});

	$('input[name=phone]').mask("+9 (999) 999-99-99");

	$(".fancybox").fancybox();

	$('.fancybox-media').fancybox({
		openEffect  : 'none',
		closeEffect : 'none',
		helpers : {
			media : {}
		}
	});
})