function checkPassword(){
    var password= document.getElementById('password').value;
    var confirmPassword=document.getElementById('c_password').value;
    var message = document.getElementById("passwordMatchMessage");

    if(password === confirmPassword){
        message.style.color="green";
        message.textContent="Password Match!";
    }

    else{

        message.style.color="red";
        message.textContext="Password do not match!"

    }

}



function checkUsername(){
    document.getElementById("username").addEventListener("input", function() {
        var username = this.value;
        
        // Make an AJAX request to check username uniqueness
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/check_username/?username=" + username, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                var usernameError = document.getElementById("usernameError");
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    if (response.unique) {
                        usernameError.textContent = "";
                    } else {
                        usernameError.textContent = "This username is already taken.";
                    }
                } else {
                    usernameError.textContent = "An error occurred while checking username.";
                }
            }
        };
        xhr.send();
    });
}

function toggleDropdown(event) {
    const dropdown = event.currentTarget.parentElement;
    dropdown.classList.toggle('open');
    const arrowIcon = event.target.querySelector('.arrow_icon');
    arrowIcon.classList.toggle('rotate');
  }


let isSidebarVisible= false;
function toggleSidebars(){
    const sidebar= document.getElementById('sidebar');
    console.log(sidebar);
    const content = document.getElementById('content');
    if(isSidebarVisible){
        sidebar.classList.add('collapsed');
        content.classList.add('expanded');

    }
    else{
        sidebar.classList.remove('collapsed');
        content.classList.remove('expanded');

    }
    isSidebarVisible = !isSidebarVisible;

} 



function toggleSidebar(){
    
    var sidebar=document.getElementById('sidebar');
    var mainContent = document.getElementById('mainContent');

    sidebar.classList.toggle("closed");

    if(sidebar.classList.contains("closed")){
        mainContent.style.marginLeft="0";


    }
    else{
        mainContent.style.marginLeft="16.66667% ";
    }
}


// function toggleSidebar(){
//     var sidebar=document.getElementById('sidebar');
//     sidebar.classList.toggle('closed');
// }

// function closeSidebar(){
//     var sidebar = document.getElementsById('sidebar');
//     sidebar.classList.add('closed');
// } 



