function checkForm() {
            var flag = true;
            flag = (
                checkFname() &&
                checkLname() &&
                checkUname() &&
                checkPass() &&
                checkEmail() &&
                checkBday() &&
                checkLoc() &&
                checkGender() &&
            )
            return flag;
        }


        function checkFname() {
            var fname = document.getElementById("firstname").value;
            var flag = true;
            if (fname == "") {
                alert("Please enter a first name");
                flag = false;
            }
            if (fname[0] != fname[0].toUpperCase()) {
                alert("First name must start with a capital letter");
                flag = false;
            }
            var letters = /^[A-Za-z\s]+$/;
            if (!(fname.match(letters))) {
                flag = false;
                window.alert("First name cannot contain spaces, numbers or special characters");
            }
            return flag;
        }


        function checkLname() {
            var letters = /^[A-Za-z\s]+$/;
            var flag = true;
            var lname = document.getElementById("lastname").value;
            if (lname == "") {
                window.alert("Please enter a last name");
                flag = false;
            }
            if (lname[0] != lname[0].toUpperCase()) {
                window.alert("Last name must start with a capital letter");
                flag = false;
            }
            if (!lname.match(letters)) {
                flag = false;
                window.alert("Last name cannot contain spaces or special characters");
            }
            return flag;
        }


        function checkUname() {
            var flag = true;
            var uname = document.getElementById("newuser").value;
            if (uname.length < 4) {
                flag = false;
                window.alert("Username must be at least 4 characters long");
            }
            var nums_letters = /^[A-Za-z0-9]+$/;
            if (!uname.match(nums_letters)) {
                flag = false;
                window.alert("Username must include only numbers and letters");
            }
            return flag;
        }


        function checkPass() {
            var flag = true;
            var rules = [
                /[0-9]/,
                /[a-z]/,
                /[A-Z]/,
                /[{!@#$%^&*}<>]/
            ];
            var pass = document.getElementById("newpass").value;
            if (pass.length < 6) {
                flag = false;
                window.alert("Password must contain at least 6 characters");
            }
            var passflag = false;
            for (var i = 0; i < rules.length; i++) {
                if (!rules[i].test(pass)) {
                    flag = false;
                    passflag = true;
                }
            }
            if (passflag == true) {
                window.alert("password must contain at least one capital letter, a lowercase letter, a number, and at least one special character !@#$%^&*");
            }
            var passcheck = document.getElementById("passconfirm").value;
            if (passcheck != pass) {
                window.alert("Password confirmation field must be identical to password");
                flag = false;
            }
            return flag;
        }


        function checkEmail() {
            var flag = true;
            var letters = /^[A-Za-z\s]+$/;
            var email = document.getElementById("mail").value;
            var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            if (!email.match(mailformat)) {
                window.alert("Email must start with a letter, contain an @ character and include a valid domain");
                flag = false;
            }
            var fmail = email[0];
            if (!fmail.match(letters)) {
                window.alert("Email address must start with a letter");
                flag = false;
            }
            return flag;

        }

        function checkBday() {
            var flag = true;
            var Bday = document.getElementById("birthday").value;
            if (Bday == "") {
                window.alert("Please enter your birthday");
                flag = false;
            }
            return flag;
        }

        function checkLoc() {
            var flag = true;
            var loc = document.getElementById("loc").value;
            if (loc == "") {
                window.alert("Please enter your location");
                flag = false;
            }
            return flag;
        }

        function checkGender() {
            var flag = false;
            var radios = document.getElementsByName("gender");
            for (var radio of radios) {
                if (radio.checked) {
                    flag = true;
                }
            }
            return flag;
        }