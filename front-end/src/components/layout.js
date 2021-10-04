import React from "react";

const Layout = ({ children }) => {
  return (
    <div id="home">
      {children}
      <nav className="navbar  navbar-default" role="navigation">
        <div className="container">
          <div className="navbar-header">
            <button
              type="button"
              className="navbar-toggle collapsed"
              data-toggle="collapse"
              data-target="#bs-example-navbar-collapse-1"
            >
              <span className="sr-only">Toggle navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
            <a className="navbar-brand" href="#">
            </a>
          </div>

          <div
            className="collapse navbar-collapse navbar-right"
            id="bs-example-navbar-collapse-1"
          >
            <ul className="nav navbar-nav">
              <li>
                <a href="#">Home </a>
              </li>
              <li>
                <a href="#">Rooms & Tariff</a>
              </li>
              <li>
                <a href="#">Introduction</a>
              </li>
              <li>
                <a href="#">Gallery</a>
              </li>
              <li>
                <a href="#">Contact</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="banner">
        <img
          src="https://images.ctfassets.net/pnliwdxhy0tx/3aFOGLztfsEAnRpNNyeiPS/de655e9ea465d597b1e88dc98ab28590/transformacion-de-medellin.jpg"
          className="img-responsive"
          alt="slide"
        />
        <div className="welcome-message">
          <div className="wrap-info">
            <div className="information">
              <h1 className="animated fadeInDown">Hotel California</h1>
              <p className="animated fadeInUp">
                We are programmed to receive. You can check-out any time you
                like, But you can never leave!
              </p>
            </div>
            <a
              href="#information"
              className="arrow-nav scroll wowload fadeInDownBig"
            >
              <i className="fa fa-angle-down"></i>
            </a>
          </div>
        </div>
      </div>

      <div id="information" className="spacer reserve-info ">
        <div className="container">
          <div className="row">
            <div className="col-sm-7 col-md-8">
              <div className="embed-responsive embed-responsive-16by9 wowload fadeInLeft">
                <iframe
                  className="embed-responsive-item"
                  title="w"
                  src="//player.vimeo.com/video/55057393?title=0"
                  width="100%"
                  height="400"
                  frameBorder="0"
                ></iframe>
              </div>
            </div>
            <div className="col-sm-5 col-md-4">
              <h3>Reservation</h3>
              <form className="wowload fadeInRight">
                <div className="form-group">
                  <input
                    type="text"
                    className="form-control"
                    placeholder="Name"
                  />
                </div>
                <div className="form-group">
                  <input
                    type="email"
                    className="form-control"
                    placeholder="Email"
                  />
                </div>
                <div className="form-group">
                  <input
                    type="Phone"
                    className="form-control"
                    placeholder="Phone"
                  />
                </div>
                <div className="form-group">
                  <div className="row">
                    <div className="col-xs-6">
                      <select className="form-control">
                        <option>No. of Rooms</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                      </select>
                    </div>
                    <div className="col-xs-6">
                      <select className="form-control">
                        <option>No. of Adult</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div className="form-group">
                  <div className="row">
                    <div className="col-xs-4">
                      <select
                        className="form-control col-sm-2"
                        name="expiry-month"
                        id="expiry-month"
                      >
                        <option>Date</option>
                        <option value="01">1</option>
                        <option value="02">2</option>
                        <option value="03">Mar (03)</option>
                        <option value="04">Apr (04)</option>
                        <option value="05">May (05)</option>
                        <option value="06">June (06)</option>
                        <option value="07">July (07)</option>
                        <option value="08">Aug (08)</option>
                        <option value="09">Sep (09)</option>
                        <option value="10">Oct (10)</option>
                        <option value="11">Nov (11)</option>
                        <option value="12">Dec (12)</option>
                      </select>
                    </div>
                    <div className="col-xs-4">
                      <select
                        className="form-control col-sm-2"
                        name="expiry-month"
                        id="expiry-month"
                      >
                        <option>Month</option>
                        <option value="01">Jan (01)</option>
                        <option value="02">Feb (02)</option>
                        <option value="03">Mar (03)</option>
                        <option value="04">Apr (04)</option>
                        <option value="05">May (05)</option>
                        <option value="06">June (06)</option>
                        <option value="07">July (07)</option>
                        <option value="08">Aug (08)</option>
                        <option value="09">Sep (09)</option>
                        <option value="10">Oct (10)</option>
                        <option value="11">Nov (11)</option>
                        <option value="12">Dec (12)</option>
                      </select>
                    </div>
                    <div className="col-xs-4">
                      <select className="form-control" name="expiry-year">
                        <option value="13">2013</option>
                        <option value="14">2014</option>
                        <option value="15">2015</option>
                        <option value="16">2016</option>
                        <option value="17">2017</option>
                        <option value="18">2018</option>
                        <option value="19">2019</option>
                        <option value="20">2020</option>
                        <option value="21">2021</option>
                        <option value="22">2022</option>
                        <option value="23">2023</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div className="form-group">
                  <textarea
                    className="form-control"
                    placeholder="Message"
                    rows="4"
                  ></textarea>
                </div>
                <button className="btn btn-default">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div className="spacer services wowload fadeInUp">
        <div className="container">
          <div className="row">
            <div className="col-sm-4">
              <div
                id="RoomCarousel"
                className="carousel slide"
                data-ride="carousel"
              >
                <div className="carousel-inner">
                  <div className="item active">
                    <img
                      src="images/photos/8.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/9.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/10.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                </div>

                <a
                  className="left carousel-control"
                  href="#RoomCarousel"
                  role="button"
                  data-slide="prev"
                >
                  <i className="fa fa-angle-left"></i>
                </a>
                <a
                  className="right carousel-control"
                  href="#RoomCarousel"
                  role="button"
                  data-slide="next"
                >
                  <i className="fa fa-angle-right"></i>
                </a>
              </div>
              <div className="caption">
                Rooms
                <a href="" className="pull-right">
                  <i className="fa fa-edit"></i>
                </a>
              </div>
            </div>

            <div className="col-sm-4">
              <div
                id="TourCarousel"
                className="carousel slide"
                data-ride="carousel"
              >
                <div className="carousel-inner">
                  <div className="item active">
                    <img
                      src="images/photos/6.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/3.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/4.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                </div>

                <a
                  className="left carousel-control"
                  href="#TourCarousel"
                  role="button"
                  data-slide="prev"
                >
                  <i className="fa fa-angle-left"></i>
                </a>
                <a
                  className="right carousel-control"
                  href="#TourCarousel"
                  role="button"
                  data-slide="next"
                >
                  <i className="fa fa-angle-right"></i>
                </a>
              </div>
              <div className="caption">
                Tour Packages
                <a href="#" className="pull-right">
                  <i className="fa fa-edit"></i>
                </a>
              </div>
            </div>

            <div className="col-sm-4">
              <div
                id="FoodCarousel"
                className="carousel slide"
                data-ride="carousel"
              >
                <div className="carousel-inner">
                  <div className="item active">
                    <img
                      src="images/photos/1.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/2.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                  <div className="item  height-full">
                    <img
                      src="images/photos/5.jpg"
                      className="img-responsive"
                      alt="slide"
                    />
                  </div>
                </div>

                <a
                  className="left carousel-control"
                  href="#FoodCarousel"
                  role="button"
                  data-slide="prev"
                >
                  <i className="fa fa-angle-left"></i>
                </a>
                <a
                  className="right carousel-control"
                  href="#FoodCarousel"
                  role="button"
                  data-slide="next"
                >
                  <i className="fa fa-angle-right"></i>
                </a>
              </div>
              <div className="caption">
                Food and Drinks
                <a href="#" className="pull-right">
                  <i className="fa fa-edit"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <footer className="spacer">
        <div className="container">
          <div className="row">
            <div className="col-sm-5">
              <h4>Tiffany-twisted</h4>
              <p>
                On a dark desert highway, cool wind in my hair Warm smell of
                colitas, rising up through the air Up ahead in the distance, I
                saw a shimmering light My head grew heavy and my sight grew dim
                I had to stop for the night There she stood in the doorway; I
                heard the mission bell And I was thinking to myself, "This could
                be Heaven or this could be Hell" Then she lit up a candle and
                she showed me the way There were voices down the corridor, I
                thought I heard them say...{" "}
              </p>
            </div>

            <div className="col-sm-3">
              <h4>Quick Links</h4>
              <ul className="list-unstyled">
                <li>
                  <a href="">Rooms & Tariff</a>
                </li>
                <li>
                  <a href="#">Introduction</a>
                </li>
                <li>
                  <a href="#">Gallery</a>
                </li>
                <li>
                  <a href="#">Tour Packages</a>
                </li>
                <li>
                  <a href="#">Contact</a>
                </li>
              </ul>
            </div>
            <div className="col-sm-4 subscribe">
              <h4>Subscription</h4>
              <div className="input-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Enter email id here"
                />
                <span className="input-group-btn">
                  <button className="btn btn-default" type="button">
                    Get Notify
                  </button>
                </span>
              </div>
              <div className="social">
                <a href="#">
                  <i
                    className="fa fa-facebook-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="facebook"
                  ></i>
                </a>
                <a href="#">
                  <i
                    className="fa fa-instagram"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="instragram"
                  ></i>
                </a>
                <a href="#">
                  <i
                    className="fa fa-twitter-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="twitter"
                  ></i>
                </a>
                <a href="#">
                  <i
                    className="fa fa-pinterest-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="pinterest"
                  ></i>
                </a>
                <a href="#">
                  <i
                    className="fa fa-tumblr-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="tumblr"
                  ></i>
                </a>
                <a href="#">
                  <i
                    className="fa fa-youtube-square"
                    data-toggle="tooltip"
                    data-placement="top"
                    data-original-title="youtube"
                  ></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </footer>

      <a href="#home" className="toTop scroll">
        <i className="fa fa-angle-up"></i>
      </a>
      <div
        id="blueimp-gallery"
        className="blueimp-gallery blueimp-gallery-controls"
      >
        <div className="slides"></div>
        <h3 className="title">title</h3>
        <a className="prev">‹</a>
        <a className="next">›</a>
        <a className="close">×</a>
      </div>
    </div>
  );
};

export default Layout;
