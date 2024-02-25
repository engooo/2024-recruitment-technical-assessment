const jsonData = [
    {
      "course_prefix": "COMP",
      "course_code": 1511,
      "course_title": "Programming Fundamentals",
      "average_stars": 4.8,
      "total_reviews": 68,
      "offered_terms": ["Term 1", "Term 2", "Term 3"]
    },
    {
      "course_prefix": "COMP",
      "course_code": 1531,
      "course_title": "Software Engineering Fundamentals",
      "average_stars": 3.9,
      "total_reviews": 47,
      "offered_terms": ["Term 1", "Term 2", "Term 3"]
    },
    {
      "course_prefix": "COMP",
      "course_code": 1521,
      "course_title": "Computer Systems Fundamentals",
      "average_stars": 4,
      "total_reviews": 40,
      "offered_terms": ["Term 1", "Term 2", "Term 3"]
    },
    {
      "course_prefix": "COMP",
      "course_code": 2521,
      "course_title": "Data Structures and Algorithms",
      "average_stars": 4,
      "total_reviews": 36,
      "offered_terms": ["Summer", "Term 1", "Term 2", "Term 3"]
    },
    {
      "course_prefix": "COMP",
      "course_code": 2511,
      "course_title": "Object-Oriented Design & Programming",
      "average_stars": 3,
      "total_reviews": 33,
      "offered_terms": ["Term 1", "Term 2", "Term 3"]
    },
    {
      "course_prefix": "COMP",
      "course_code": 3311,
      "course_title": "Database Systems",
      "average_stars": 4,
      "total_reviews": 33,
      "offered_terms": ["Term 1", "Term 3"]
    }
  ]

// Generate course cards
const cardContainer = document.querySelector('.card-container');
const cardTemplate = document.getElementById("card-template");
jsonData.forEach(course => {
    const courseCard = cardTemplate.cloneNode(true);
    const courseCode = course.course_prefix + course.course_code

    courseCard.removeAttribute("id");
    courseCard.setAttribute("card-id", courseCode)

    // Populate cards with json information
    courseCard.querySelector("#course").textContent = courseCode
    
    const starsWidth = (course.average_stars / 5) * 100;
    
    courseCard.querySelector("#avg-stars").style.width = starsWidth + '%';
    courseCard.querySelector("#total-reviews").textContent = course.total_reviews + " reviews"
    courseCard.querySelector("#course-title").textContent = course.course_title

    // Append card to cards container
    cardContainer.append(courseCard)

    // Generate terms offered for each card
    course.offered_terms.forEach(term => {
      const termContainer = courseCard.querySelector("#term-container");
      const termOffered = courseCard.querySelector("#offered-term-template").cloneNode(true)
      termOffered.style.display = 'inline'
      termOffered.removeAttribute("id");
      termOffered.textContent = term.toString()
      
      termContainer.append(termOffered)
    })
})

// Strech Task 1: Change colour of title
const title = document.getElementById("title");
title.addEventListener('click', () => {
  title.style.color = 'purple'
})

// Stretch Task 2
const searchbar = document.getElementById("search-bar");
const overlay = document.getElementById("task-overlay");
searchbar.addEventListener('click', () => {
  overlay.style.display = "block"
})

const dismiss = document.getElementById("dismiss");
dismiss.addEventListener('click', () => {
  overlay.style.display = "none"
})