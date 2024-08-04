let register_screen = document.querySelector("#register-screen")
let login_screen = document.querySelector("#login-screen")

register_screen.style.display = 'none'
login_screen.style.display = 'block'
document.querySelector("#register-tab").style.background = 'transparent'
document.querySelector("#login-tab").style.background = 'white'

document.querySelector("#register-tab").addEventListener("click", ()=>{
	login_screen.style.display = 'none'
	register_screen.style.display = 'block'
	document.querySelector("#login-tab").style.background = 'transparent'
	document.querySelector("#register-tab").style.background = 'white'
})
document.querySelector("#login-tab").addEventListener("click", ()=>{
	register_screen.style.display = 'none'
	login_screen.style.display = 'block'
	document.querySelector("#register-tab").style.background = 'transparent'
	document.querySelector("#login-tab").style.background = 'white'
})

document.querySelector("#geetest").addEventListener("click", ()=>{
	document.querySelector(".geetest_wait_dot").style.animation = "geetestAnimation 10s infinite linear"
	setTimeout(()=>{
		document.querySelector(".geetest_wait_dot").style.animation = ""
		document.querySelector(".geetest_wait_dot").style.background = 'rgb(1 206 8)'
		document.querySelector(".geetest_class").innerHTML = 'Captcha Verified Successfully'
		setTimeout(()=>{
			document.querySelector("#geetest").style.display = 'none'
		} , 5000)
	} , 10000)
})

document.querySelectorAll(".status_text").forEach(s => {
    setTimeout(()=>{
        s.style.display = 'none'
    }, 4000)
})  

document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop - 50, // Adjust for header height
                behavior: "smooth",
            });
        });
    }
});

const countrySelect = document.getElementById('countrySelect');

// Replace 'countries.json' with the actual path to your JSON file
fetch('../static/countries.json')
    .then(response => response.json())
    .then(data => {
    data.forEach(country => {
        const option = document.createElement('option');
        option.value = country.code; // Replace 'code' with the appropriate property
        option.text = country.name; // Replace 'name' with the appropriate property
        countrySelect.appendChild(option);
    });
    })
    .catch(error => {
    console.error('Error fetching countries:', error);
    });
