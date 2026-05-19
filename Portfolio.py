import streamlit as st


st.set_page_config(
    page_title="Diyotima Ghosh | Full Stack Developer & AI/ML Enthusiast",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    /* Base App Overrides */
    .stApp {
        background-color: #03010a;
        color: #ffffff;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Top Header Navigation Mockup */
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background: rgba(15, 5, 30, 0.8);
        padding: 12px;
        border-radius: 10px;
        border-bottom: 2px solid #ff00cc;
        box-shadow: 0 0 15px rgba(255, 0, 204, 0.3);
        margin-bottom: 30px;
    }
    .nav-item {
        color: #00cfff;
        text-decoration: none;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 1px;
    }
    .nav-item:hover {
        color: #ff00cc;
        text-shadow: 0 0 8px #ff00cc;
    }

    /* Glow Typography */
    .glow-text {
        color: #ff00cc;
        text-shadow: 0 0 10px #ff00cc, 0 0 20px #ff00cc;
    }

    /* Main Layout Cards */
    .cyber-container {
        border: 2px solid #20003b;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        background: rgba(11, 4, 22, 0.75);
        box-shadow: 0 0 15px rgba(32, 0, 59, 0.6);
        transition: all 0.3s ease-in-out;
    }
    .cyber-container:hover {
        border-color: #00cfff;
        box-shadow: 0 0 20px rgba(0, 207, 255, 0.4);
    }

    /* Container Section Headings */
    .section-header {
        font-size: 22px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 8px;
    }

    /* Dynamic Contact Boxes */
    .contact-box {
        border: 2px solid #00cfff;
        padding: 14px;
        border-radius: 12px;
        margin-top: 15px;
        background: rgba(0, 0, 0, 0.5);
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.15);
        font-size: 15px;
        text-align: left;
        transition: 0.3s;
    }
    .contact-box:hover {
        border-color: #ff00cc;
        box-shadow: 0 0 15px rgba(255, 0, 204, 0.5);
    }

    /* Custom Tech Skill Badges */
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .skill-tag {
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 600;
        background: rgba(5, 2, 10, 0.8);
        transition: 0.3s;
    }
    .badge-blue { border: 1.5px solid #00cfff; color: #00cfff; box-shadow: 0 0 5px rgba(0,207,255,0.2); }
    .badge-pink { border: 1.5px solid #ff00cc; color: #ff00cc; box-shadow: 0 0 5px rgba(255,0,204,0.2); }
    .badge-green { border: 1.5px solid #00ffcc; color: #00ffcc; box-shadow: 0 0 5px rgba(0,255,204,0.2); }

    /* Interactive Project Item Blocks */
    .project-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: 0.3s;
    }
    .project-card:hover {
        background: rgba(255, 255, 255, 0.05);
        transform: translateX(4px);
    }
    .project-info {
        padding-right: 15px;
    }
    .project-btn {
        background: transparent;
        color: white;
        border: 1.5px solid #ff00cc;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        white-space: nowrap;
        cursor: pointer;
        box-shadow: 0 0 8px rgba(255,0,204,0.3);
    }
    .project-card:hover .project-btn {
        background: #ff00cc;
        box-shadow: 0 0 12px #ff00cc;
    }

    /* Core Matrix Grid Footer Layout */
    .core-skills-wrapper {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 10px;
        text-align: center;
        margin-top: 15px;
    }
    .core-skill-item {
        background: rgba(255,255,255,0.02);
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #20003b;
        font-size: 13px;
    }
    .core-skill-item span {
        display: block;
        font-size: 22px;
        margin-bottom: 5px;
    }

    /* Smooth rounded targeting directly for Streamlit image element styles */
    .stImage img {
        border: 3px solid #ff00cc;
        border-radius: 25px;
        box-shadow: 0 0 15px #ff00cc, 0 0 25px #00cfff;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="nav-bar">
    <a class="nav-item" href="#about-me">🏠 ABOUT</a>
    <a class="nav-item" href="#technical-skills">⚙️ SKILLS</a>
    <a class="nav-item" href="#experience">💼 EXPERIENCE</a>
    <a class="nav-item" href="#projects">📁 PROJECTS</a>
    <a class="nav-item" href="#education">🎓 EDUCATION</a>
    <a class="nav-item" href="#certifications">🏅 CERTIFICATIONS</a>
    <a class="nav-item" href="#connect">✉️ CONTACT</a>
</div>
""", unsafe_allow_html=True)


hero_left, spacer_column, hero_right = st.columns([1.3, 0.1, 0.8], vertical_alignment="center")

with hero_left:
    st.markdown("""
    <div style="padding-top:10px;">
        <h1 class="glow-text" style="font-size:95px; line-height:0.9; margin-bottom:0px; font-weight:800;">DIYOTIMA</h1>
        <h1 style="font-size:95px; line-height:0.9; margin-top:-5px; color:#00cfff; text-shadow:0 0 8px #00cfff, 0 0 20px #00cfff; font-weight:800;">GHOSH</h1>
    </div>
    <div style="font-size:18px; margin-top:15px; margin-bottom:20px; color:#ffffff; font-weight: 400; line-height: 1.4;">
        Full Stack Developer || Core & Advanced Java || Spring Boot || React || JavaScript || MySQL & MongoDB || Passionately mentoring and training students to become technically strong and industry-ready
    </div>
    """, unsafe_allow_html=True)


    cx1, cx2 = st.columns(2)
    with cx1:
        st.markdown('<div class="contact-box">📧 &nbsp; diyotimaghosh03@gmail.com</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-box">🐙 &nbsp; github.com/DiyotimaGhosh</div>', unsafe_allow_html=True)
    with cx2:
        st.markdown('<div class="contact-box">📞 &nbsp; +91 7595942443</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-box">📍 &nbsp; India</div>', unsafe_allow_html=True)

with spacer_column:
    st.write("")  # Serves as a buffer to expand the layout horizon horizontally

with hero_right:

    st.image(
        "Image.jpeg",
        use_container_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)


col_left, col_right = st.columns([1.1, 1.1], gap="large")


with col_left:

    st.markdown("""
    <div id="about-me" class="cyber-container">
        <div class="section-header" style="color: #ff00cc;">👤 About Me</div>
        <p style="color: #dcd6e8; line-height: 1.6; font-size:14.5px; text-align: justify; margin-bottom:12px;">
           I am a passionate Full Stack Developer and AI/ML Enthusiast with hands-on experience in software development & I possess strong expertise in designing and developing high-performance & AI enhanced web applications using Advanced Java, Spring Boot & it's microservices, React, JavaScript, MySQL, and MongoDB. I have built efficient, user-centric digital solutions, implementing modern software development practices, and exploring AI/ML-driven technologies to create innovative applications. I also train and mentor aspiring students to become technically sound and career oriented. 
           <br><br>
           Started my professional journey as a Python Developer Intern at Kabadi Techno, where I gained hands-on experience in backend development, scalable application development using Python, and real-world problem-solving. Worked with Stream lit for application development and deployment, while also gaining exposure to API integration, database operations, automation scripting, and agile development practices.
           <br><br>
           Later, I worked with Swami Vivekananda University as a Technical Trainer & Software Developer, where I contributed to developing AI-enhanced web applications using React and Spring Boot. Worked on building responsive frontend interfaces with React and JavaScript, along with scalable backend services and RESTful APIs using Spring Boot and Advanced Java. Alongside development, I also trained students in modern technologies and Full Stack Development.
           <br><br>
           Currently working with Amity University as a Software Trainer, mentoring aspiring developers in Java, Full Stack Development, and modern software technologies.
           <br><br>
           I am specialized in building scalable, efficient, and user-friendly web applications using Java, Spring Boot, React, JavaScript, and modern frontend technologies. With strong knowledge of REST APIs, database management, and backend architecture, I enjoy transforming complex business requirements into clean and high-performance solutions.
           <br><br>
           I thrive in collaborative environments, value clean coding practices, and continuously explore emerging technologies in AI/ML, Data Science, and Software Engineering to enhance my technical expertise and deliver impactful solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)


    with st.container():
        st.markdown('<div id="experience" class="cyber-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header" style="color: #00cfff;">💼 Experience</div>', unsafe_allow_html=True)


        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <span style="color:#ff00cc; font-weight:700; font-size:16px;">1. Technical Trainer & Software Developer</span>
            <span style="color:#a59fb0; font-size:13px;">Jul '24 - Sept '25</span>
        </div>
        <div style="color:#00cfff; font-size:14px; margin-bottom:10px; font-weight:500;">Swami Vivekananda University</div>
        """, unsafe_allow_html=True)

        st.write("""
        I have worked with Swami Vivekananda University as a Technical Trainer & Software Developer where I along with the team, developed  AI enhanced web application for the organization using React And Spring Boot. I contributed extensively for the development by creating responsive, user-friendly interfaces with React, JavaScript, and modern UI practices, while developing scalable backend services and RESTful APIs using Spring Boot and Advanced Java.  I have used a microservices-based architecture to ensure modularity, scalability, and efficient service management across applications. Further I implemented secure authentication and authorization mechanisms using JWT authentication tokens and role-based access control to enhance application security. Integrated API Gateway architecture was used for centralized request handling, routing, and security management across multiple services and utilized Feign Client for seamless inter-service communication within distributed systems and optimized backend performance for high availability and maintainability. Used Hybrid databases & I also gained exposure to cloud-based deployment environments, application hosting, and modern development workflows including version control, debugging, testing, and deployment strategies. 

Alongside development, my responsibilities also included actively mentoring students in Full Stack Development, helping them strengthen their technical, logical, and project development skills through practical learning and real-world implementation approaches.
        """)

        st.markdown("<br>", unsafe_allow_html=True)


        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <span style="color:#ff00cc; font-weight:700; font-size:16px;">2. Senior Technical Trainer</span>
            <span style="color:#a59fb0; font-size:13px;">Sept '25 - Present</span>
        </div>
        <div style="color:#00cfff; font-size:14px; margin-bottom:10px; font-weight:500;">Amity University</div>
        """, unsafe_allow_html=True)

        st.write("""
        After gaining 1 year of experience in software development and 1 year of teaching experience as a Technical Trainer at Swami Vivekananda University, I transitioned to Amity University as a Senior Technical Trainer to further expand my expertise in technical education and industry-oriented training.

In this role, I continue to mentor and train students to become industry-ready professionals and prepare them for placement opportunities. I deliver training in Java Full Stack Development, MERN Stack, MEAN Stack, Data Structures & Algorithms (DSA), AI/ML, and Data Science, focusing on both conceptual understanding and real-world project implementation.

My responsibilities also include preparing question papers, evaluating answer scripts, managing classroom operations, conducting technical mentoring sessions, and creating a productive learning environment for students. Additionally, I contribute to the development of recorded tutorial content and learning resources to ensure uninterrupted and accessible learning for students beyond classroom sessions.
        """)

        st.markdown("<br>", unsafe_allow_html=True)


        st.markdown("""
        <div style="color:#00ffcc; font-weight:700; font-size:13px; letter-spacing:1px; margin-bottom:6px;">INTERNSHIP</div>
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <span style="color:#ffffff; font-weight:600; font-size:15px;">Python Developer Intern</span>
            <span style="color:#a59fb0; font-size:13px;">Jun '23 - May '24</span>
        </div>
        <div style="color:#00cfff; font-size:13px; margin-bottom:10px;">Kabadi Techno</div>
        """, unsafe_allow_html=True)

        st.write("""
        I along with my team was responsible for developing and maintaining backend applications using Python while working in projects. Additionally my responsibilities included authentication and authorization mechanisms using JWT tokens, secure API handling, debugging, testing, and agile development practices.

My role included working on REST API integration, automation scripting and resolving technical issues to improve application efficiency and maintainability. I collaborated with team members in an agile development environment, participated in code reviews, and contributed to problem-solving discussions for improving software architecture and application workflows.

I also worked on light weight APIs such as Stream lit-based applications for rapid development and deployment, along with database integration and management using Oracle, SQL, and NoSQL databases.
        """)

        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("""
    <div id="education" class="cyber-container">
        <div class="section-header" style="color: #00ffcc;">🎓 Education</div>
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <span style="color:#ff00cc; font-weight:700; font-size:16px;">B.Tech, Computer Science</span>
            <span style="color:#a59fb0; font-size:13px;">Jul '20 - May '24</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom:10px;">
            <span style="color:#00cfff; font-weight:500; font-size:14px;">Kalinga Institute of Industrial Technology</span>
            <span style="color:#00ffcc; font-weight:700; font-size:14px;">Grade: 8.78</span>
        </div>
        <ul style="color: #dcd6e8; padding-left:20px; font-size:14px;">
            <li style="margin-bottom:4px;">Served as Board Member of the Public Speaking, Debate, and Elocution Society and represented the university in various competitions.</li>
            <li style="margin-bottom:4px;">Strong foundation in programming, data structures, algorithms, DBMS, OS, networks, and web technologies.</li>
            <li style="margin-bottom:4px;">Worked on projects involving Java, Python, Full Stack Development, and problem-solving concepts.</li>
            <li>Actively participated in technical activities, public speaking and collaborative learning environments.</li>
        </ul>
    </div>
    """,
                unsafe_allow_html=True)


with col_right:

    with st.container():
        st.markdown('<div id="technical-skills" class="cyber-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header" style="color: #00cfff;">⚙️ Technical Skills</div>',
                    unsafe_allow_html=True)

        skills_list = [
            ("Advanced Java", "badge-blue"), ("JavaScript", "badge-blue"), ("TypeScript", "badge-pink"),
            ("React", "badge-pink"),
            ("Spring Boot", "badge-blue"), ("Spring MVC", "badge-pink"), ("Spring Data JPA", "badge-pink"),
            ("Hibernate", "badge-pink"),
            ("Microservices", "badge-blue"), ("REST APIs", "badge-blue"), ("JWT", "badge-blue"), ("RBAC", "badge-blue"),
            ("API Gateway", "badge-blue"), ("Feign Client", "badge-pink"), ("HTML5", "badge-blue"),
            ("CSS3", "badge-blue"),
            ("Tailwind CSS", "badge-pink"), ("Bootstrap", "badge-pink"), ("MySQL", "badge-blue"),
            ("MongoDB", "badge-pink"),
            ("Oracle", "badge-pink"), ("SQL", "badge-blue"), ("NoSQL", "badge-blue"), ("Streamlit", "badge-green"),
            ("Python", "badge-pink"), ("AI/ML", "badge-pink"), ("Data Science", "badge-pink"),
            ("Power BI", "badge-pink"),
            ("Tableau", "badge-pink"), ("Postman", "badge-pink"), ("Git & GitHub", "badge-blue"),
            ("Agile", "badge-pink")
        ]

        html_buffer = '<div class="skills-grid">'
        for skill, cls in skills_list:
            html_buffer += f'<span class="skill-tag {cls}">{skill}</span>'
        html_buffer += '</div>'

        st.markdown(html_buffer, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


    with st.container():
        st.markdown('<div id="projects" class="cyber-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header" style="color: #ff00cc;">📁 Projects</div>', unsafe_allow_html=True)
        
with st.container():
        st.markdown('<div id="projects" class="cyber-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header" style="color: #ff00cc;">📁 Projects</div>', unsafe_allow_html=True)

        projects_data = [{"title": "Education Platform (Coding Updesh)",
             "desc": "I developed a full-stack education platform where students can access content and explore quizzes. I used Angular, Spring Boot, MySQL & MongoDB.",
             "border": "#00cfff",
             "url": "https://codingupdesh.web.app/"},
            {"title": "Wallet Management System",
             "desc": "I built a Student Wallet Management System using Spring Boot and databases to help students track income, expenses, and savings effectively.",
             "border": "#00ffcc",
             "url": "https://github.com/DiyotimaGhosh/Wallet-Management"},
            {"title": "Movie Application Database",
             "desc": "I designed and implemented a normalized relational database schema (MySQL) for a movie application to manage users, movies, bookings, and transactions.",
             "border": "#ff00cc",
             "url": "https://github.com/DiyotimaGhosh/Movie-Application-"},
            {"title": "Ordering Application",
             "desc": "I created a Pizza Ordering Application in Python where users can place multiple orders in a single session and view the total bill.",
             "border": "#ffaa00",
             "url": "https://github.com/DiyotimaGhosh/Ordering-Application"},
            {"title": "Women Safety Application (Safe Nest)",
             "desc": "I developed a console-based safety application in Java to provide immediate help and security features for users in distress.",
             "border": "#00cfff",
             "url": "https://github.com/DiyotimaGhosh/Women-Safety-Application"}
            
        ]

      
        for proj in projects_data:
            st.markdown(f"""
            <div class="project-card" style="border-left: 4px solid {proj['border']};">
                <div class="project-info">
                    <div style="font-weight:700; color:{proj['border']}; font-size:15px; margin-bottom:4px;">{proj['title']}</div>
                    <div style="font-size:13px; color:#cfc9da; line-height:1.4;">{proj['desc']}</div>
                </div>
                <a href="{proj['url']}" target="_blank" class="project-link-wrapper">
                    <div class="project-btn">View Project ➔</div>
                </a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("""
    <div id="certifications" class="cyber-container">
        <div class="section-header" style="color: #00ffcc;">🏅 Certifications</div>
        <ul style="color:#dcd6e8; font-size:14px; padding-left:20px; margin:0;">
            <li style="margin-bottom:6px;">Managing Database Queries – <strong>NIIT Limited</strong></li>
            <li>Java Full Stack – <strong>NIIT Limited</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div id="connect" class="cyber-container">
        <div class="section-header" style="color: #00cfff;">🚀 Let's Connect</div>
        <p style="font-size:13.5px; color:#cfc9da; margin-bottom:15px;">I'm always open to discussing new opportunities, collaborations, and innovative projects.</p>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; font-size:12px;">
            <div style="border:1px solid #ff00cc; padding:8px; border-radius:6px; background:rgba(0,0,0,0.3);">✉️ diyotimaghosh03@gmail.com</div>
            <div style="border:1px solid #ff00cc; padding:8px; border-radius:6px; background:rgba(0,0,0,0.3);">🔗 linkedin.com/in/diyotima-ghosh</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div class="cyber-container">
    <div class="section-header" style="color: #ffaa00; text-align:center;">🌟 Core Skills</div>
    <div class="core-skills-wrapper">
        <div class="core-skill-item"><span>💡</span><strong>Problem Solving</strong></div>
        <div class="core-skill-item"><span>🧠</span><strong>Critical Thinker</strong></div>
        <div class="core-skill-item"><span>🚀</span><strong>Innovative</strong></div>
        <div class="core-skill-item"><span>🤝</span><strong>Resilient</strong></div>
        <div class="core-skill-item"><span>👥</span><strong>Team Player</strong></div>
        <div class="core-skill-item"><span>💬</span><strong>Communicator</strong></div>
        <div class="core-skill-item"><span>👑</span><strong>Leader</strong></div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="text-align: center; font-size: 20px; font-style: italic; color: #ff00cc; text-shadow: 0 0 8px rgba(255,0,204,0.4); margin-top: 30px; margin-bottom: 5px;">
    “ I love building solutions that make a difference and solving problems that matter. ”
</div>
""", unsafe_allow_html=True)
