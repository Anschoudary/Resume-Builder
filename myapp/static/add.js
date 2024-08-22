console.log('Hello World')

document.querySelector('.edu-btn').addEventListener('click', (e) => {
     e.preventDefault();
    let edu = document.createElement('div')
        edu.innerHTML = `<h3>Educational Info</h3>
                    Degree:* <input type="text" name="degree" id="">
                    College:* <input type="text" name="college" id="">
                    Year:* <input type="number" name="degree_year" id="">`;

    document.querySelector('.educational').appendChild(edu);

     });