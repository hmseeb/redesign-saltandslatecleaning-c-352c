# -*- coding: utf-8 -*-
"""Shared site data for the Salt & Slate static site generator."""

BIZ = {
    "name": "Salt & Slate Cleaning Company",
    "short": "Salt & Slate",
    "phone": "(385) 333-7737",
    "tel": "+13853337737",
    "sms_body": "Hi%2C%20I%27d%20like%20to%20get%20a%20quote",
    "email": "hello@saltandslatecleaning.com",
    "rating": "5.0",
    "reviews": "263",
    "locations": "6",
    "form_action": "https://vision.leadrai.com/api/forms/a152d8cf19bb1a85f595f17580def3b9",
    "instagram": "https://www.instagram.com/saltandslatecleaningcompany/",
    "facebook": "https://www.facebook.com/saltandslatecleaning",
    "year": "2026",
}

OFFICES = [
    ("Salt Lake City", "159 W Broadway, Suite 200", "Salt Lake City, UT 84101", "(385) 333-7737", "+13853337737"),
    ("Park City", "1743 Sidewinder Dr, Suite 1027", "Park City, UT 84060", "(435) 800-0377", "+14358000377"),
    ("Scottsdale", "4310 N 75th St, Suite #135", "Scottsdale, AZ 85251", "(623) 745-2729", "+16237452729"),
    ("Draper", "13867 S Bangerter Pkwy, Suite 202", "Draper, UT 84020", "(385) 374-1222", "+13853741222"),
    ("Las Vegas", "3930 University Center Dr, Suite 807", "Las Vegas, NV 89119", "(725) 777-1406", "+17257771406"),
    ("Frisco", "8855 Preston Trace Blvd, Suite 250", "Frisco, TX 75034", "(945) 222-3213", "+19452223213"),
]

# slug, label, short tagline
RESIDENTIAL = [
    ("recurring-cleaning", "Standard &amp; Recurring Cleaning", "Weekly, biweekly, or monthly home cleaning"),
    ("deep-cleaning", "Deep Cleaning", "One-time intensive cleaning"),
    ("move-in-cleaning", "Move-In Cleaning", "New home prep before unpacking"),
    ("move-out-cleaning", "Move-Out Cleaning", "Lease-end and pre-sale cleaning"),
    ("vacation-home-cleaning", "Vacation Home Cleaning", "Seasonal prep and guest-ready care"),
    ("airbnb-cleaning", "Airbnb &amp; Rental Cleaning", "Same-day turnover for hosts"),
    ("estate-cleaning", "Estate Cleaning", "White-glove luxury home care"),
    ("specialty-cleaning", "Specialty Cleaning", "Premium surface and feature care"),
    ("post-construction-cleaning", "Post-Construction Cleaning", "The final clean before move-in"),
]

# slug (None = page not built), label, description
COMMERCIAL = [
    ("office-cleaning", "Office Cleaning",
     "Commercial office cleaning across Utah, Arizona, and Nevada."),
    ("medical-office-cleaning", "Medical Office Cleaning",
     "Commercial cleaning for medical offices and outpatient practices across Utah, Arizona, and Nevada."),
    ("dental-office-cleaning", "Dental Office Cleaning",
     "Commercial cleaning for dental practices across Utah, Arizona, and Nevada."),
    ("law-firm-cleaning", "Law Firm Cleaning",
     "After-hours commercial cleaning for legal offices across Utah, Arizona, and Nevada."),
    ("gym-cleaning", "Gym &amp; Fitness Cleaning",
     "Commercial cleaning for gyms, fitness centers, and 24/7-access facilities across Utah, Arizona, and Nevada."),
    ("restaurant-cleaning", "Restaurant Cleaning",
     "After-hours commercial cleaning for restaurants and kitchens across Utah, Arizona, and Nevada."),
    ("warehouse-cleaning", "Warehouse Cleaning",
     "Commercial cleaning for warehouses, distribution centers, and fulfillment facilities across Utah, Arizona, and Nevada."),
    ("retail-cleaning", "Retail Cleaning",
     "Commercial cleaning for retail stores and showrooms across Utah, Arizona, and Nevada."),
    (None, "Church Cleaning",
     "Recurring cleaning for sanctuaries, fellowship halls, classrooms, and nursery areas."),
    (None, "Event Venue Cleaning",
     "Pre-event setup cleaning and post-event restoration for wedding venues, banquet halls, corporate event spaces, and private event facilities."),
    (None, "Property Management Cleaning",
     "Common area maintenance for apartment complexes, condos, and HOAs across Utah, Arizona, and Nevada."),
    (None, "Daycare Cleaning",
     "After-hours commercial cleaning for licensed childcare facilities across Utah, Arizona, and Nevada."),
    (None, "Salon &amp; Spa Cleaning",
     "Commercial cleaning for salons and spas across Utah, Arizona, and Nevada."),
    (None, "Coworking Space Cleaning",
     "Shared kitchen, hot desk, phone booth, and conference room cleaning for modern flexible workspaces."),
    (None, "Commercial Construction Cleanup",
     "Post-construction final cleaning — dust removal, residue removal, and inspection-ready detail — for commercial renovation and new build projects."),
]

STATES = [
    ("utah", "Utah", "Premium residential and commercial cleaning across Utah's most desirable communities."),
    ("arizona", "Arizona", "Luxury home and commercial cleaning in Arizona's premier communities across Maricopa County."),
    ("nevada", "Nevada", "Premium cleaning services for Las Vegas Valley's most exclusive communities and businesses."),
    ("texas", "Texas", "Premium residential and commercial cleaning across the Dallas-Fort Worth metroplex, from the Park Cities and Preston Hollow to the master-planned communities of Collin County and the TX-114 corporate corridor."),
]

PICKER = [
    ("Keep my home consistently clean", "Regular visits once your home is at maintenance condition.",
     "Recurring cleaning", "/services/recurring-cleaning/"),
    ("Catch up on buildup", "More detail on baseboards, cabinet fronts, doors and bathroom grout.",
     "Deep cleaning", "/services/deep-cleaning/"),
    ("Get ready to move", "An empty-home clean, including inside cleared cabinets and appliances.",
     "Move-out cleaning", "/services/move-out-cleaning/"),
    ("Prepare for the next guest", "Cleaning between bookings, with linen and access needs agreed in advance.",
     "Airbnb turnover cleaning", "/services/airbnb-cleaning/"),
    ("Clean my workplace", "A scope and schedule built around your workspace and business hours.",
     "Office cleaning", "/commercial/office-cleaning/"),
    ("Finish a build or remodel", "A final clean for construction dust after the trades have finished.",
     "Post-construction cleaning", "/services/post-construction-cleaning/"),
]

# Home-page "why us" blocks
WHY = [
    ("Same Standard Every Visit",
     "A detailed room-by-room checklist on every cleaning so the standard, the coverage, and the satisfaction guarantee stay the same from visit to visit."),
    ("Licensed, Background-Checked &amp; Insured",
     "Salt &amp; Slate is a licensed and fully insured cleaning company. Every cleaner passes a comprehensive background check before stepping foot in your home."),
    ("Decades of Experience",
     "Our team members bring decades of professional cleaning experience to every home and business we serve."),
    ("24-Hour Satisfaction Guarantee",
     "If anything falls short, we return to make it right at no additional charge. No fine print."),
]

HOW_IT_WORKS = [
    ("01", "Get Your Quote",
     "Tell us about your property. We'll send you flat-rate pricing so you know the full cost upfront — no surprises."),
    ("02", "Cleaner Standards",
     "Every Salt &amp; Slate cleaner is licensed, background-checked, and fully insured. We brief them on your home — which surfaces need special care, where you want extra attention, what to skip."),
    ("03", "Enjoy the Results",
     "The same detailed checklist on every visit, backed by our 24-hour satisfaction guarantee. If anything's not right, we come back at no charge."),
]

RECOGNIZED = [
    ("The Watch Party",
     "Six weeks of recurring service at Salt Lake City's Civic Center event hub during the inaugural Watch Party event series, February through March 2026."),
    ("Salt Lake City Mayor's Office",
     "Commissioned by the Salt Lake City Mayor's Office as recurring commercial cleaning partner for a high-profile civic event series in downtown Salt Lake City."),
    ("Major Studio Productions",
     "Recurring residential service for Park City and Deer Valley luxury estates — including private homes used as on-location sets by HBO and other major film and television studios."),
]

HOME_STATE_CITIES = {
    "utah": ("Park City · Coalville · Kamas · Francis · Oakley · Henefer · Midway · Heber City", "+ 42 more cities"),
    "arizona": ("Scottsdale · Paradise Valley · Fountain Hills · Phoenix · Cave Creek · Gilbert · Chandler · Carefree", "+ 9 more cities"),
    "nevada": ("Henderson · Las Vegas · Summerlin · Boulder City · North Las Vegas", ""),
    "texas": ("Dallas · Highland Park · University Park · Coppell · Irving · Addison · Richardson · Frisco", "+ 26 more cities"),
}

# Before / after pairs available in images/source (webp + jpg fallbacks)
BEFORE_AFTER = [
    ("Luxury kitchen clean", "15-img-2487-1754950975730", "16-img-2487-1754950975730",
     "17-img-2519-1754950975730", "18-img-2519-1754950975730",
     "Luxury kitchen before a Salt &amp; Slate clean", "The same luxury kitchen after a Salt &amp; Slate clean"),
    ("Kitchen deep clean", "19-img-2489-1754950987754", "20-img-2489-1754950987754",
     "21-img-2521-1754950987754", "22-img-2521-1754950987754",
     "Kitchen before a Salt &amp; Slate deep clean", "Kitchen after a Salt &amp; Slate deep clean"),
    ("Refrigerator deep clean", "23-img-2579-1754951015393", "24-img-2579-1754951015393",
     "25-img-2575-1754951015393", "26-img-2575-1754951015393",
     "Refrigerator interior before a Salt &amp; Slate deep clean", "Refrigerator interior after a Salt &amp; Slate deep clean"),
    ("Refrigerator refresh", "27-img-2578-1754951015393", "28-img-2578-1754951015393",
     "29-img-2572-1754951015393", "30-img-2572-1754951015393",
     "Refrigerator shelves before a Salt &amp; Slate refresh", "Refrigerator shelves after a Salt &amp; Slate refresh"),
    ("Post-construction clean", "31-img-4761-1764112803329", "32-img-4761-1764112803329",
     "33-img-4757-1764112803330", "34-img-4757-1764112803330",
     "Room covered in construction dust before Salt &amp; Slate post-construction cleaning",
     "The same room after Salt &amp; Slate post-construction cleaning"),
    ("Sink deep clean", "35-img-4783-1764259564770", "36-img-4783-1764259564770",
     "37-img-4784-1764259564769", "38-img-4784-1764259564769",
     "Kitchen sink with buildup before a Salt &amp; Slate deep clean", "Kitchen sink restored after a Salt &amp; Slate deep clean"),
]

# name, quote, when
REVIEWS = [
    ("Jayme Trevino", "I am happy with my experience! Scheduling was easy and flexible. The deep cleaning was very thorough and my house looks great!", "4 months ago"),
    ("Hannah Montiel", "Thank you so much for a wonderful job cleaning. Ana was so thorough and communicative with how she cleaned. The house smells amazing!", "6 months ago"),
    ("Sarah Speaks", "Tammy was absolutely lovely. Communicative and focused on all the (very problematic) areas we discussed. Even gave tips on keeping up with some of the tougher issues with hard water. I’m absolutely booking again and grateful.", "7 months ago"),
    ("Brian Tully", "Really happy with the level of service and customer service. After some less than satisfactory experience with another company, we have switched over to Salt and Slate, and are really much happier. Our cleaner, Tammy, is really thorough.", "7 months ago"),
    ("Kelsey Blackstone", "Both cleaners were fantastic! I will definitely be using this service again. They were efficient and paid attention to detail. They were very respectful of my home and belongings. I am expecting a little one and haven’t had any energy to deep clean.", "7 months ago"),
    ("Tara Kushlan", "I loved using Salt and Slate cleaning company. They responded right away and got me on the schedule for a deep clean. Flaviana did a fantastic job with my home — everything was spotless and it was such a relief walking into a truly sparkling space.", "7 months ago"),
    ("Mare Bregman", "I used Salt and Slate for our Move-In Cleaning. They did a great job among the chaos of furniture deliveries, internet service install and my husband directing all of it. They managed to get every corner despite many moving parts.", "10 months ago"),
    ("Dallis Christensen", "I was so relieved to find out that Salt and Slate Cleaning opened a location in Park City. They have been my go-to commercial cleaner for my office in Salt Lake City, and I needed someone to clean my remote office in Park City as well.", "10 months ago"),
    ("Brody Vecera", "Tammy did a great job deep cleaning my townhouse in Millcreek. My floors, carpet, counters, and bathrooms look much better. She even cleaned out a nasty vent in my ceiling that will probably help my breathing moving forward.", "8 months ago"),
    ("Megan Neiderhiser", "We were very pleased with our first time deep clean. Our house hadn’t been cleaned in months and with kids and winter weather we needed an overhaul. We’re excited to set up service with Salt &amp; Slate. They are very prompt and professional.", "8 months ago"),
    ("Anna Knott", "Miriam and Reyna were very kind, thorough and professional. Thank you!", "8 months ago"),
    ("Lacey Fontaneau", "We hired them to do a post construction clean for our new construction 5,000 square foot house in Holladay. It was a multi day project and we could not be happier. The cleaners were professional, on time and took a lot of pride in their work.", "9 months ago"),
    ("Audrey Vander Most", "WOW. Carmen and Michelle are absolute magicians. Professional, thorough, communicative, and polite. I keep catching all the little things they cleaned and realizing how much better it all looks. Highly recommend!", "9 months ago"),
    ("Gonzalo C", "I hired their services to do a deep clean after a pest issue was cleared and Tami did a phenomenal job. Every little special request was met and she was great with my dog who typically is not a stranger pup. Will use again.", "9 months ago"),
    ("James Landers", "Fantastic — no hassle cleaning company with really lovely cleaners. I received a move-in clean with Salt and Slate for my home in Alpine. The booking form was easy, received a text within a few minutes and was given a quote.", "10 months ago"),
    ("Amberli Newman", "We had a move in/move out cleaning service done at our rental in West Valley City and we were very satisfied with the service. Would highly recommend and use again when we need a rental cleaned in between tenants.", "10 months ago"),
    ("Kate Andrus", "We needed someone to come in and deep clean my mom’s home while she was in the hospital. Carmen and Michelle did an absolutely fabulous job. They went above and beyond to make the home ready for her. I highly recommend them!", "11 months ago"),
    ("Ashley Chou", "Michelle did a fantastic job. I don’t think my house has ever been so clean in its existence. Smelled so fresh and clean when I walked in. Easy to book with for a same-day appointment and service was done faster than promised.", "12 months ago"),
    ("Tim", "I recently hired Salt &amp; Slate Cleaning Company in Salt Lake City and was absolutely blown away with their service. From start to finish, it was flawless. The cleaning team arrived right on time, greeted us warmly, and were respectful of our home.", "a year ago"),
    ("Zane Busteed", "I recently hired Salt &amp; Slate Cleaning Company for a deep clean of my home in Salt Lake City, and I couldn’t be more impressed. From the moment I scheduled the appointment, their team was super responsive and accommodating with my busy schedule.", "a year ago"),
    ("Dallis Christensen", "I had Salt and Slate come clean my law office in downtown Salt Lake City and they did a great job. I am going to switch to them as my new recurring service. I was pleasantly surprised — they look like they specialize in residential, but they do a lot of commercial cleaning as well.", "a year ago"),
    ("Vasean Norwood", "As a pet owner, it’s important to my health and their health that the space they live in is organic and clean. Harsh chemicals was something I wanted to avoid. With Salt and Slate they tackled the grime, pet hair, and dander.", "a year ago"),
    ("Mark Conroy", "I own a high end Airbnb in Park City and we were recommended Salt and Slate Cleaning. Marta and her team are very thorough. They even left local Utah honey, chocolates and a candle after our first clean. This company understands customer service.", "a year ago"),
    ("Amber LaBrizzi", "At first I was skeptical about which cleaning company would be right for me and my needs. That is when I met Marta at Salt and Slate, and I will never look anywhere else. They exceeded my expectations from the start. Customer service was incredible.", "a year ago"),
    ("Julia Clark", "They are the best at post construction. Had our 10000 sq ft home renovated and we were very impressed by the ladies attention to detail! Worth every penny", "5 months ago"),
    ("Ashley Hughes", "The ladies saved me so much time. I was able to unpack some things while they tackled the deep cleaning, which was so helpful. They did a great job with the key areas like oven, and bathrooms! Will have them back to do the full apartment once we finish unpacking!", "a year ago"),
    ("Marc Pardee", "Did a deep cleaning for our whole house for the first time in a long time after some renovation work. Really impressed with the communication of the team, the cleaning team did a walkthrough with us before and after, and there was clear expectations on what kind of work was included vs out of scope. The team was effic", "3 months ago"),
    ("Alexis Wien", "They came in after a mold restoration and shower renovation project, my home was SO dusty. I just walked in and am super impressed! The place looks completely different and it smells great. I’m grateful I chose them to do my post construction cleaning.", "2 months ago"),
    ("Hannah Speer", "I had my initial deep clean done for my apartment and it looks and smells amazing! I love that they had two people come because it got the job done very quickly, but they were also efficient. I will be booking for recurring!", "3 months ago"),
    ("Neal Bermeyer", "We interviewed a few different companies for a post construction clean of our Westlake home and ultimately chose salt and slate cleaning company due to fabulous reviews and before/after photos. They did a great job. They now service our home for bi-weekly cleans.", "a week ago"),
    ("Evans Evans", "Orlando our cleaner was thorough and such a sweet person. Wonderful move in clean for our apartment in Dallas. Easy to schedule and easy to pay", "6 days ago"),
    ("Tyler Skinner", "Not only great cleaning but great customer service! Highly recommend", "today"),
    ("Christopher Ellis", "Excellent service, left the house sparkling and was very reasonable in terms of pricing and availability.", "today"),
]

HERO_SLIDES = [
    ("00-hero-home", "01-hero-home",
     "Studio McGee-style living room with white sectional, wood beams, and herringbone fireplace, freshly cleaned by Salt &amp; Slate"),
    ("02-carousel-kitchen", "03-carousel-kitchen",
     "Pristine Studio McGee-style kitchen with marble waterfall island and brass pendants, freshly cleaned by Salt &amp; Slate"),
    ("04-carousel-primary-bedroom", "05-carousel-primary-bedroom",
     "Pristine Studio McGee-style primary bedroom with made bed and linen bedding, freshly cleaned by Salt &amp; Slate"),
    ("06-carousel-primary-bathroom", "07-carousel-primary-bathroom",
     "Pristine Studio McGee-style primary bathroom with marble and freestanding tub, freshly cleaned by Salt &amp; Slate"),
    ("08-carousel-foyer", "09-carousel-foyer",
     "Pristine Studio McGee-style grand foyer with sweeping oak staircase, freshly cleaned by Salt &amp; Slate"),
    ("10-carousel-office", "11-carousel-office",
     "Pristine professional office interior, reset and cleaned by Salt &amp; Slate commercial cleaning teams"),
]

# path -> (jpg_basename_or_None, webp_basename_or_None, alt)
PAGE_HERO = {
    "/services/": ("02-carousel-kitchen", "03-carousel-kitchen",
                   "Pristine kitchen with marble waterfall island, freshly cleaned by Salt &amp; Slate residential teams"),
    "/services/recurring-cleaning/": ("00-hero-home", "01-hero-home",
                                      "Living room kept spotless by Salt &amp; Slate recurring house cleaning"),
    "/services/deep-cleaning/": ("21-img-2521-1754950987754", "22-img-2521-1754950987754",
                                 "Kitchen counters and cabinets after a Salt &amp; Slate deep clean"),
    "/services/move-in-cleaning/": ("08-carousel-foyer", "09-carousel-foyer",
                                    "Grand foyer and oak staircase cleaned by Salt &amp; Slate before move-in"),
    "/services/move-out-cleaning/": ("37-img-4784-1764259564769", "38-img-4784-1764259564769",
                                     "Kitchen sink scrubbed to a shine during a Salt &amp; Slate move-out cleaning"),
    "/services/vacation-home-cleaning/": (None, "14-luxuryhome3-1764622946784",
                                          "Mountain-view living room of a vacation home maintained by Salt &amp; Slate"),
    "/services/airbnb-cleaning/": ("04-carousel-primary-bedroom", "05-carousel-primary-bedroom",
                                   "Guest bedroom reset with fresh linens for an Airbnb turnover by Salt &amp; Slate"),
    "/services/estate-cleaning/": (None, "13-luxuryhom2-1764622932087",
                                   "Marble floors and grand entryway of a Utah estate cleaned by Salt &amp; Slate"),
    "/services/specialty-cleaning/": ("06-carousel-primary-bathroom", "07-carousel-primary-bathroom",
                                      "Marble primary bathroom and freestanding tub given specialty surface care by Salt &amp; Slate"),
    "/services/post-construction-cleaning/": ("33-img-4757-1764112803330", "34-img-4757-1764112803330",
                                              "Interior cleared of construction dust after Salt &amp; Slate post-construction cleaning"),
    "/commercial/": ("10-carousel-office", "11-carousel-office",
                     "Professional office interior reset and cleaned by Salt &amp; Slate commercial cleaning teams"),
    "/commercial/office-cleaning/": ("10-carousel-office", "11-carousel-office",
                                     "Office workstations and common areas cleaned by Salt &amp; Slate commercial crews"),
    "/commercial/law-firm-cleaning/": ("10-carousel-office", "11-carousel-office",
                                       "Professional legal office interior cleaned after hours by Salt &amp; Slate"),
    "/about/": ("12-why-salt-and-slate", None,
                "Salt &amp; Slate cleaning professional at work in a luxury kitchen"),
}

SHOWCASE = [
    (None, "13-luxuryhom2-1764622932087", "Luxury home marble floors and grand entryway in Utah", "Luxury Homes"),
    (None, "14-luxuryhome3-1764622946784", "Luxury home living room with mountain views in Utah", "Homes Over 10,000 Sq Ft"),
]
