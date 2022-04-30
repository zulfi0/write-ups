function show_upload_local_file(argument) {
    var form_div = document.getElementById('form-div');
    form_div.innerHTML = `
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" class="file">
            <input name="local" type="hidden" value='1'>
            <br>
            <br>
            <button id="submit-local" type="submit" class="submit">Submit</button>
        </form>
        `;
}

function show_upload_remote_file(argument) {
    var form_div = document.getElementById('form-div');
    form_div.innerHTML = `
    <br><br>
        <form action="/upload" method="POST" enctype="application/x-www-form-urlencoded" >
            <input type="textbox" name="url" class="textbox">
            <input name="remote" type="hidden" value='1'>
            <br>
            <br>
            <button id="submit-remote" type="submit" class="submit">Submit</button>
        </form>
        `;
}
