<!doct
ype html>
<html>
<head>
    <title>LUPKOIN</title>
    <link rel="shortcut icon" type="image/jpg" href="../static/cropped_logo.png"/>
</head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
    body {
        font-family: "Lato", sans-serif
    }
</style>

<body>
<!-- Navbar -->
<div class="w3-top">
    <div class="w3-bar w3-light-grey w3-card">
        <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right"
           href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i
                    class="fa fa-bars"></i></a>
        <a class="w3-bar-item w3-button w3-opacity w3-padding-large">HOME</a>
        <a href="send" class="w3-bar-item w3-button w3-padding-large w3-hide-small">SEND</a>
        <a href="receive" class="w3-bar-item w3-button w3-padding-large w3-hide-small">RECEIVE</a>
        <a onclick="signIn()" class="w3-bar-item w3-button w3-padding-large w3-hide-small w3-right">Login</a>

        <a href="javascript:void(0)" class="w3-padding-large w3-hover-red w3-hide-small w3-right"><i
                    class="fa fa-search"></i></a>
    </div>
</div>

<!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
<div id="navDemo" class="w3-bar-block w3-light-grey w3-hide w3-hide-large w3-hide-medium w3-top"
     style="margin-top:46px">
    <a href="send" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">SEND</a>
    <a href="receive" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">RECEIVE</a>
</div>

<!-- Page content -->
<div class="w3-content" style="max-width:2000px;margin-top:46px">
    <br>
    <div class="w3-center">
        <a href="/">
            <img class="w3-center" src="../static/cropped_logo.png" alt="lk_logo" height="100" width="100"/>
        </a></div>
    <h1 class="w3-wide w3-center">LUPKOIN</h1>
    <h4 class="w3-wide w3-opacity w3-center">A Safe & Secure P2P Coin</h4>
    <hr>

    <div class="w3-container w3-content w3-padding-32" style="max-width:800px" id="contact">
        <h3 class="w3-wide w3-center">CREATE NEW WALLET</h3>
        <div class="w3-center">
            <button class="w3-button w3-center-align w3-section" style="width:50%; background-color: #4184f4;
    color: #ffffff" href="#create_wallet"
                    onclick="document.getElementById('id01').style.display='block'">
                CREATE
            </button>
        </div>
        <br>
        <p class="w3-opacity w3-center"><i>Already have a wallet? <a href="#sign-in" onclick="signIn()">Sign
                    in</i></a></p>
    </div>

</div>

{#modal for create wallet#}
<div class="w3-container">
    <div id="id01" class="w3-modal">
        <div class="w3-modal-content w3-card-4 w3-animate-zoom" style="max-width:600px">
            <div class="w3-center"><br>
                <span onclick="document.getElementById('id01').style.display='none'"
                      class="w3-button w3-xlarge w3-hover-red w3-display-topright" title="Close Modal">&times;</span>
                <label><b>Create New Wallet</b></label>
            </div>

            <form id="new-wallet-form" class="w3-container" action="register.php" method="post">
                <div class="w3-section">
                    <label><b>Email</b></label>
                    <input class="w3-input w3-border w3-margin-bottom" type="email" placeholder="Enter Email"
                           name="email" id="email" required>
                    <label><b>Password</b></label>
                    <input class="w3-input w3-border w3-margin-bottom" type="password" placeholder="Enter Password"
                           name="password" id="password" pattern="^\S{6,}$"
                           onchange="this.setCustomValidity(this.validity.patternMismatch ? 'Must have at least 6 characters' : ''); if(this.checkValidity()) form.password_two.pattern = this.value ?;"
                           required>
                    <label><b>Verify Password</b></label>
                    <input class="w3-input w3-border" type="password" pattern="^\S{6,}$" id="password_two"
                           placeholder="Verify Password"
                           name="password_two" required oninput="check(this)">

                    <button class="w3-button w3-block  w3-section w3-padding" style="background-color: #4184f4;
    color: #ffffff" id="new-wallet-submit" type="submit" onclick="createWallet()">Login
                    </button>
                    <input class="w3-check w3-margin-top w3-grey" type="checkbox" checked="checked"> Remember me
                </div>

                <div class="w3-container w3-border-top w3-padding-16 w3-light-grey">
                    <button onclick="document.getElementById('id01').style.display='none'" type="button"
                            class="w3-button w3-grey">Cancel
                    </button>
                    <span class="w3-right w3-padding w3-hide-small">Forgot <a href="#">password?</a></span>
                </div>
            </form>
        </div>
    </div>

    {#modal for sign in#}
    <div class="w3-container">
        <div id="id02" class="w3-modal">
            <div class="w3-modal-content w3-card-4 w3-animate-zoom" style="max-width:600px">
                <div class="w3-center"><br>
                    <span onclick="document.getElementById('id02').style.display='none'"
                          class="w3-button w3-xlarge w3-hover-red w3-display-topright"
                          title="Close Modal">&times;</span>
                    <label><b>Sign In</b></label>
                </div>

                {#                <form class="w3-container" id="form-submit">#}
                    <div class="w3-section">
                        <label><b>Username</b></label>
                        <input class="w3-input w3-border w3-margin-bottom" type="text" placeholder="Enter Username"
                               name="usrname" required>
                        <label><b>Password</b></label>
                        <input class="w3-input w3-border" type="password" placeholder="Enter Password" name="psw"
                               required>
                        <button class="w3-button w3-block w3-section w3-padding" style="background-color: #4184f4;
    color: #ffffff" type="submit" onclick="createWallet()">Login
                        </button>
                        <input class="w3-check w3-margin-top w3-grey" type="checkbox" checked="checked"> Remember me
                    </div>
                    {#                </form>#}

                <div class="w3-container w3-border-top w3-padding-16 w3-light-grey">
                    <button onclick="document.getElementById('id02').style.display='none'" type="button"
                            class="w3-button w3-grey">Cancel
                    </button>
                    <span class="w3-right w3-padding w3-hide-small">Forgot <a href="#">password?</a></span>
                </div>

            </div>
        </div>
    </div>

    <script>
        function myFunction() {
            var x = document.getElementById("navDemo");
            if (x.className.indexOf("w3-show") == -1) {
                x.className += " w3-show";
            } else {
                x.className = x.className.replace(" w3-show", "");
            }
        }

        function signIn() {
            document.getElementById('id02').style.display = 'block'
        }


        {#create wallet javascript#}

        function createWallet() {
            document.getElementById('id01').style.display = 'none'
        };

        {#click outside of modal to close#}
        var modal = document.getElementById('id01');
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

    </script>

</body>
</html>
