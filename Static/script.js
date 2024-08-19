//Designed by Sophie McAlavey
document.addEventListener("DOMContentLoaded", function () {
    // Show the onboarding overlay as soon as the page loads
    document.getElementById("onboarding-overlay").style.display = "flex";

    // Show the first step of the onboarding process
    document.getElementById("step-1").style.display = "block";
});

function nextStep(step) {
    // Hide all steps
    var steps = document.getElementsByClassName("onboarding-step");
    for (var i = 0; i < steps.length; i++) {
        steps[i].style.display = "none";
    }

    // Show the selected step
    document.getElementById("step-" + step).style.display = "block";
}

function closeOnboarding() {
    // Hide the onboarding overlay
    document.getElementById("onboarding-overlay").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript is loaded and ready to go!");

});

function validateForm() {
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");

    // Basic validation example
    if (nameInput.value.trim() === "") {
        alert("Name cannot be empty.");
        nameInput.focus();
        return false;
    }

    if (!validateEmail(emailInput.value)) {
        alert("Please enter a valid email address.");
        emailInput.focus();
        return false;
    }

    // Form is valid
    return true;
}

function validateEmail(email) {
    // Simple email validation pattern
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}
