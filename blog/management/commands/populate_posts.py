from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = 'This is the post data'
    
    def handle(self, *args, **options):
        
        
      titles = [
        
    "From DOS to Windows 11,",
    "Connecting the world,",
    "Stay safe in the digital jungle,",
    "The web that powers everything,",
    "Machines that think,",
    "Write once, run everywhere,",
    "Organize to optimize,",
    "Beyond the hard drive,",
    "It’s what’s inside that counts,",
    "Build the web, brick by brick,",
    "Hack the right way,",
    "Where science meets the impossible,",
    "Code your future,",
    "Your identity, online,",
    "Data is the new oil,",
    "Learning to learn,",
    "Track, save, collaborate,",
    "From idea to deployment,",
    "Step into the future,",
    "Small screens, big ideas,"
]


      
      
      contents = [
          
                        "Operating systems are the core of any computing device,They manage hardware, run applications, and provide a user interface,From simple command lines to modern GUIs, they’ve come a long way",

                "Computer networks link devices together to share data and resources,They range from small home networks to massive global systemsThey are the foundation of today’s connected world",

                "Cybersecurity protects systems from unauthorized access and digital threats,It involves firewalls, encryption, antivirus tools, and ethical hacking,In a digital age, safety starts with awareness",

                "The internet is a network of networks using protocols to transfer data,It powers websites, emails, video calls, and more, A truly invisible force behind modern life",

                "Artificial Intelligence enables machines to mimic human thinking,It powers voice assistants, smart cameras, and recommendation engines,AI is revolutionizing how we work, learn, and live",

                "Python is known for its clean syntax and wide range of applications,It’s great for web development, data science, automation, and AI, A perfect choice for beginners and pros alike",

                "Data structures like lists, stacks, and trees help organize information,They boost code efficiency, speed, and performance, Mastering them is key to smart programming",

                "Cloud computing provides on-demand access to data and services online, It eliminates the need for bulky local servers or storage, Flexible, scalable, and cost-effective",

                "Computer hardware includes components like CPU, RAM, and storage drivesEach part has a role in processing, storing, or displaying data, Understanding hardware helps in repairs and upgrades",

                "Web development involves building websites using HTML, CSS, and JavaScript, It brings design and function together for users on all devices, It’s a skill in demand across the globe",

                "Ethical hacking is the legal way to find and fix security flaws, It helps companies stay protected against cyberattacks Hack with purpose, not for harm",

                "Quantum computing uses the power of qubits to perform fast calculations, It holds potential to solve problems classical computers can’t handle A revolutionary leap in computation",
                "Programming languages are tools to communicate with machines, Each has its strengths: Python for simplicity, C++ for speed, JS for web,  Choosing the right one shapes your project",

                "A portfolio website is your personal brand on the internet, It shows your work, skills, and achievements to employers and clients, A powerful tool for career growth",

                "Databases store, manage, and retrieve digital data efficiently, Used in websites, apps, and software, they keep data structured,  From MySQL to MongoDB, data stays organized",

                "AI, Machine Learning, and Deep Learning help machines make decisions,  They power everything from Netflix recommendations to medical diagnoses, Smarter systems start with smarter models",

                "Git is a version control system that tracks code changes over time,  It’s perfect for collaborating, fixing bugs, and managing versions,  A developer’s time machine",

                "SDLC stands for Software Development Life Cycle, It outlines steps like planning, development, testing, and deployment, It ensures projects stay on track and on quality",

                "Virtual Reality creates immersive 3D digital environments,It’s used in gaming, training, and therapy to simulate real experiences, Step into a new dimension",

                "Mobile app development puts your ideas into users’ hands,Using tools like Flutter and React Native, you can build for Android and iOS, Small screens, huge possibilities",


      ]
      
      
      img_urls = [
            'https://picsum.photos/id/1/800/400',
            'https://picsum.photos/id/2/800/400',
            'https://picsum.photos/id/3/800/400',
            'https://picsum.photos/id/4/800/400',
            'https://picsum.photos/id/5/800/400',
            'https://picsum.photos/id/6/800/400',
            'https://picsum.photos/id/7/800/400',
            'https://picsum.photos/id/8/800/400',
            'https://picsum.photos/id/9/800/400',
            'https://picsum.photos/id/10/800/400',
            'https://picsum.photos/id/11/800/400',
            'https://picsum.photos/id/12/800/400',
            'https://picsum.photos/id/13/800/400',
            'https://picsum.photos/id/14/800/400',
            'https://picsum.photos/id/15/800/400',
            'https://picsum.photos/id/16/800/400',
            'https://picsum.photos/id/17/800/400',
            'https://picsum.photos/id/18/800/400',
            'https://picsum.photos/id/19/800/400',
            'https://picsum.photos/id/20/800/400',

      ]
      categories = Category.objects.all()
      
      for title,content,img_url in zip(titles,contents,img_urls):
          category =  random.choice(categories)
          Post.objects.create(title = title,content = content,img_url = img_url,category = category)
          
      self.stdout.write(self.style.SUCCESS("INSERTINg THE DATA"))