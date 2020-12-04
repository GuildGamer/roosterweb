<!DOCTYPE html>

{% load static %}
{% load cart_template_tags %}

<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		 <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->

		<title>{% block head_title %}{% endblock %}</title>
    	{% block extra_head %}
    	{% endblock %}

		<!-- Google font -->
		<link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,700" rel="stylesheet">

		<!-- Bootstrap -->
		<link type="text/css" rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}"/>

		<!-- Slick -->
		<link type="text/css" rel="stylesheet" href="{% static 'css/slick.css' %}"/>
		<link type="text/css" rel="stylesheet" href="{% static 'css/slick-theme.css' %}"/>

		<!-- nouislider -->
		<link type="text/css" rel="stylesheet" href="{% static 'css/nouislider.min.css' %}"/>

		<!-- Font Awesome Icon -->
		<link rel="stylesheet" href="{%static 'css/font-awesome.min.css' %}">

		<!-- Custom stlylesheet -->
		<link type="text/css" rel="stylesheet" href="{% static 'css/style.css' %}"/>

		<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
		  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
		  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
		<![endif]-->

    </head>
	<body>
		<!-- HEADER -->
		<header>
			<!-- TOP HEADER -->
			<div id="top-header">
				<div class="container">
					<ul class="header-links pull-left">
						{% comment %}<li><<i class="fa fa-phone"></i><span style="color: white;">+234-808-439-5900</span></li>{% endcomment %}
						<li><i class="fa fa-envelope-o"></i><span style="color: white;">roosterdotcom@gmail.com</span></li>
						{%comment%}<li><i class="fa fa-map-marker"></i><span style="color: white;" class="float-right">1734 Stonecoal Road</span></li>{%endcomment%}
					</ul>
					{%comment%}
					<ul class="header-links pull-right">
						<li><a href="#"><i class="fa fa-dollar"></i>	Naira</a></li>
						<li><a href="#"><i class="fa fa-user-o"></i> My Account</a></li>
					</ul>
					{%endcomment%}
				</div>
			</div>
			<!-- /TOP HEADER -->

			<!-- NAVIGATION -->
		
			<!-- container -->
			
			
			<!-- MAIN HEADER -->
			<div id="header">
				<!-- container -->
				<div class="container">
					<!-- row -->
					<div class="row">
						<!-- LOGO -->
						<div class="col-md-3">
							<div class="header-logo">
								<a href="#" class="logo">
									<h3 style="color: #36ab13;">ROOSTER</h3>{% comment %}<img src="{% static './img/logo.png"' %} alt="">{% endcomment %}
								</a>
							</div>
						</div>
						<!-- /LOGO -->

						<!-- SEARCH BAR -->
						<div class="col-md-6 text-center">
							<div class="header-search">
								<form action="{% url 'base_app:search' %}" method="get">
									 {% csrf_token %}
									<input class="input-select text-center" style="width: 80%; background-color: #ededed;" type="search" name="search" placeholder="Search products, brands and categories">
									<button class="search-btn" type="submit"><i class="fa fa-search text-center" style="font-size: 100%;"></i></button>
								</form>
							</div>
						</div>
						<!-- /SEARCH BAR -->

						<!-- ACCOUNT -->
						<div class="col-md-3 clearfix">
							<div class="header-ctn">

								{% if request.user.is_authenticated %}
								<!-- Cart -->
								<div class="dropdown">
										<a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
											<a  href="{% url 'base_app:order-summary' %}">
												<i class="fa fa-shopping-cart"></i>
												<div class="qty">{{ request.user|cart_item_count }}</div><span>Cart</span>
											</a>
										</a>
								</div>
								{% endif %}
								{% if request.user.is_authenticated %}
								<div class="dropdown">
								<a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
								<a href="{% url 'account_logout' %}">
									<i class="fa fa-sign-out"></i>
									<span>Sign out</span>
								</a>
								</a>
								</div>
								{% else %}
								<div class="dropdown">
									<a class="dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="true">
										<i class="fa fa-user-o"></i>
										<span>Account</span>
									</a>
									<div class="cart-dropdown">
										<div class="cart-list">
										<div class="product-widget">
										<div class="cart-btns">
											
												<!-- Login -->
											<a href="{% url 'account_login' %}"><span>Sign in</span></a>
												<!-- /Login -->
				
												<!-- Sign up -->
											<a href="{% url 'account_signup' %}"><span>Sign Up</span></a>
												<!-- /Sign up -->	
											</div>
										</div>
											</div>
										</div>
									</div>
									{% endif %}
									<div class="menu-toggle">
										<a href="#">
											<i class="fa fa-bars"></i>
											<span>Menu</span>
										</a>
									</div>
								</div>
								
								
								<!-- /Cart -->
								
								

								<!-- Menu Toogle -->
								
								<!-- /Menu Toogle -->
							</div>
						</div>
						<!-- /ACCOUNT -->
					</div>
					<!-- row -->
				</div>
				<!-- container -->
			</div>
			<!-- /MAIN HEADER -->
		</header>
		<!-- /HEADER -->

		<!-- NAVIGATION -->
		<nav id="navigation">
			<!-- container -->
			<div class="container">
				<!-- responsive-nav -->
				<div id="responsive-nav">
					<!-- NAV -->
					<ul class="main-nav nav navbar-nav">
						<li class="#"><a href="/"><i class="fa fa-home"></i>Home</a></li>
						<li><a href="{% url 'base_app:sell' %}"><i class="fa fa-money"></i>Sell</a></li>
						<li><a href="#"><i class="fa fa-support"></i>Costumer care</a></li>
						{% if request.user == seller %}
						<li><a href="{% url 'base_app:store-managment' %}"><i class="fa fa-support"></i>Store managment</a></li>
						{% endif %}
						
					</ul>
					<!-- /NAV -->
				</div>
				<!-- /responsive-nav -->
			</div>
			<!-- /container -->
		</nav>
		<!-- /NAVIGATION -->
		
		{% if messages %}
		<div class="container" style="background-color: white;  border-radius: 8px; padding-top: 5px; padding-bottom: 5px; opacity: 0.6;">
		<ul class="messages">
			{% for message in messages %}
			<li {% if message.tags %} class="{{ message.tags }}" {% endif %}>{{ message }}</li>
			{% endfor %}
		</ul>
		</div>
		{% endif %}
        
        {% block content %} 
		{% endblock %}
		
		{% block extra_body %}
    	{% endblock %}

		<!-- FOOTER -->
		
		
		<footer id="footer">
			<!-- top footer -->
			<div class="section">
				<!-- container -->
				<div class="container">
					<!-- row -->
					<div class="row">
						<div class="col-md-3 col-xs-6">
							<div class="footer">
								<h3 class="footer-title">About Us</h3>
								<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut.</p>
								<ul class="footer-links">
									<li><a href="#"><i class="fa fa-map-marker"></i>1734 Stonecoal Road</a></li>
									<li><a href="#"><i class="fa fa-phone"></i>+021-95-51-84</a></li>
									<li><a href="#"><i class="fa fa-envelope-o"></i>email@email.com</a></li>
								</ul>
							</div>
						</div>

						<div class="col-md-3 col-xs-6">
							<div class="footer">
								<h3 class="footer-title">Categories</h3>
								<ul class="footer-links">
									<li><a href="#">Hot deals</a></li>
									<li><a href="#">Laptops</a></li>
									<li><a href="#">Smartphones</a></li>
									<li><a href="#">Cameras</a></li>
									<li><a href="#">Accessories</a></li>
								</ul>
							</div>
						</div>

						<div class="clearfix visible-xs"></div>

						<div class="col-md-3 col-xs-6">
							<div class="footer">
								<h3 class="footer-title">Information</h3>
								<ul class="footer-links">
									<li><a href="#">About Us</a></li>
									<li><a href="#">Contact Us</a></li>
									<li><a href="#">Privacy Policy</a></li>
									<li><a href="#">Orders and Returns</a></li>
									<li><a href="#">Terms & Conditions</a></li>
								</ul>
							</div>
						</div>

						<div class="col-md-3 col-xs-6">
							<div class="footer">
								<h3 class="footer-title">Service</h3>
								<ul class="footer-links">
									<li><a href="#">My Account</a></li>
									<li><a href="#">View Cart</a></li>
									<li><a href="#">Wishlist</a></li>
									<li><a href="#">Track My Order</a></li>
									<li><a href="#">Help</a></li>
								</ul>
							</div>
						</div>
					</div>
					<!-- /row -->
				</div>
				<!-- /container -->
			</div>
			<!-- /top footer -->

			<!-- bottom footer -->
			<div id="bottom-footer" class="section">
				<div class="container">
					<!-- row -->
					<div class="row">
						<div class="col-md-12 text-center">
							<ul class="footer-payments">
								<li><a href="#"><i class="fa fa-cc-visa"></i></a></li>
								<li><a href="#"><i class="fa fa-credit-card"></i></a></li>
								<li><a href="#"><i class="fa fa-cc-paypal"></i></a></li>
								<li><a href="#"><i class="fa fa-cc-mastercard"></i></a></li>
								<li><a href="#"><i class="fa fa-cc-discover"></i></a></li>
								<li><a href="#"><i class="fa fa-cc-amex"></i></a></li>
							</ul>
							<span class="copyright">
								<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
								Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
							<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
							</span>
						</div>
					</div>
						<!-- /row -->
				</div>
				<!-- /container -->
			</div>
			<!-- /bottom footer -->
		</footer>
		<!-- /FOOTER -->

		<!-- jQuery Plugins -->
		<script src="{% static 'js/jquery.min.js' %}"></script>
		<script src="{% static 'js/bootstrap.min.js' %}"></script>
		<script src="{% static 'js/slick.min.js' %}"></script>
		<script src="{% static 'js/nouislider.min.js' %}"></script>
		<script src="{% static 'js/jquery.zoom.min.js' %}"></script>
		<script src="{% static 'js/main.js' %}"></script>

	</body>
</html>
