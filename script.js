function generatePassword() {
    var length = document.getElementById("length").value;
    if (length < 4) {
        alert("Password length must be at least 4 characters.");
        return;
    }
    var passwordCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
    var password = "";
    for (var i = 0; i < length; i++) {
        var randomIndex = Math.floor(Math.random() * passwordCharacters.length);
        password += passwordCharacters.charAt(randomIndex);
    }
    document.getElementById("password").value = password;
}

function copyToClipboard() {
    var password = document.getElementById("password").value;
    var textarea = document.createElement("textarea");
    textarea.value = password;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    alert("Password copied to clipboard.");
}
