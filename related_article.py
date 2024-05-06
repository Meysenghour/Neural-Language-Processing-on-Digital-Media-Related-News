import spacy
import numpy as np

# Load a spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample titles (replace with your actual titles)
all_articles = [
        {
            "id": 29,
            "title": "Chea Serey the taboo, podcasts gain popularity among young Cambodians"
        },
        {
            "id": 30,
            "title": "KhmerSME Wants to Make Chea Serey Life Easier for Cambodian Small Businesses"
        },
        {
            "id": 31,
            "title": "Processing Is the Missing Link for Cambodian Fruit Exports Chea Serey"
        },
        {
            "id": 36,
            "title": "How NBC Cambodia’s Startups Surf the Uncertainty of the Global Pandemic"
        },
        {
            "id": 38,
            "title": "Bringing Small Businesses Online: an Interview With NBC Delicio Founder Socheat Yi"
        },
        {
            "id": 39,
            "title": "Announcing the Launch of Kiripost Business News That Matter More to NBC"
        },
        {
            "id": 40,
            "title": "Caffeine, Culture and Cambodianess"
        },
        {
            "id": 41,
            "title": "As Covid-19 Rules Fall, Businesses Face an Uncertain Future"
        },
        {
            "id": 42,
            "title": "Tech Dreams Fuel Disabled Student's Courageous Journey"
        },
        {
            "id": 43,
            "title": "Even Without Boat Races or Fireworks, Water Festival is a Hit"
        },
        {
            "id": 45,
            "title": "Reopening Still a Distant Promise in Cambodia’s Remote East"
        },
        {
            "id": 49,
            "title": "Tourism Industry Prepares to Welcome Back Travellers"
        },
        {
            "id": 50,
            "title": "ABA System Crash Leaves Customers Without Access to Cash"
        },
        {
            "id": 52,
            "title": "Critically-Endangered Turtles Released Into Their Natural Habitat"
        },
        {
            "id": 53,
            "title": "Phnom Penh Photo Festival Offers Local Artists a Platform to Shine"
        },
        {
            "id": 54,
            "title": "Recycling Business Aids the Kingdom’s Environment and Economy"
        },
        {
            "id": 57,
            "title": "Business Reimagined"
        },
        {
            "id": 58,
            "title": "Cambodia’s ICT Start-ups Awarded for Innovations During Covid-19"
        },
        {
            "id": 60,
            "title": "Food Safety Remains A Challenge for Agricultural Export"
        },
        {
            "id": 61,
            "title": "The US Seeks to Elevate Cambodia’s Agriculture Sector Through New USDA Office"
        },
        {
            "id": 62,
            "title": "Arts Collective Shines with Retro Flair"
        },
        {
            "id": 63,
            "title": "Prince Ranariddh’s Body Returned From France"
        },
        {
            "id": 64,
            "title": "Asia’s Lasting Love Affair with Honda Super Cub"
        },
        {
            "id": 65,
            "title": "Cambodia Urged to Embrace Industry 4.0"
        },
        {
            "id": 66,
            "title": "Late Prince Norodom Ranariddh Funeral - In Pictures"
        },
        {
            "id": 67,
            "title": "NBC Ceases Issuing MFI Licences"
        },
        {
            "id": 68,
            "title": "Cambodia Launches National Startup Program"
        },
        {
            "id": 69,
            "title": "Cambodia’s Investment in Gold Grows"
        },
        {
            "id": 70,
            "title": "Internship Fair Hopes to Help Cambodian Students Get Hired"
        },
        {
            "id": 71,
            "title": "Cambodia’s Economy Faces A Slow Recovery"
        },
        {
            "id": 72,
            "title": "Computer Campaign Aims for Education Equality"
        },
        {
            "id": 78,
            "title": "Art Festival Attracts Crowds to Temple Town"
        },
        {
            "id": 79,
            "title": "Art Festival in Siem Reap - In Pictures"
        },
        {
            "id": 80,
            "title": "Battambang Hospital Goes Online"
        },
        {
            "id": 81,
            "title": "Economic Improvements Await in 2022"
        },
        {
            "id": 82,
            "title": "Siem Reap Welcomes First International Flight"
        },
        {
            "id": 83,
            "title": "Fires Leave Communities Homeless"
        },
        {
            "id": 84,
            "title": "Siem Reap’s Top Coffee Shops for Digital Nomads"
        },
        {
            "id": 85,
            "title": "Award-winning Restaurant Sets Its Eyes on the Local Market"
        },
        {
            "id": 86,
            "title": "Stadium to Host Southeast Asian Games Opens"
        },
        {
            "id": 88,
            "title": "NagaWorld Workers Strike Over Unfair Dismissals"
        },
        {
            "id": 89,
            "title": "Phnom Penh Port Secures $12 million Profit in 2021"
        },
        {
            "id": 90,
            "title": "Pharmacist-Turned Entrepreneur Dreams of Safe Drugs for All"
        },
        {
            "id": 91,
            "title": "Water Authority Reveals Finances Late Due to Covid Case"
        },
        {
            "id": 92,
            "title": "Informal Businesses Take the Toll of Covid-19"
        },
        {
            "id": 93,
            "title": "Small Businesses Embrace Digitalisation During Pandemic"
        },
        {
            "id": 94,
            "title": "NagaWorld Union Members and Workers Continue Non-violent Strike"
        },
        {
            "id": 95,
            "title": "Challenges Remain for Siem Reap Businesses Despite the Country Reopening"
        },
        {
            "id": 96,
            "title": "Students Sit First Exams in Two Years"
        },
        {
            "id": 97,
            "title": "Baby Elephant’s Birth Gives Fresh Hopes to Elephant Population"
        },
        {
            "id": 98,
            "title": "Cambodia Should Engage with Myanmar Junta to Find Social Stability"
        },
        {
            "id": 99,
            "title": "Breastfeeding Saves Cambodia’s Economy $137 million"
        },
        {
            "id": 100,
            "title": "Kids Continue to Sell At Angkor Wat to Survive"
        },
        {
            "id": 101,
            "title": "Unions and Civil Society Call on Authorities to Release Strikers"
        },
        {
            "id": 102,
            "title": "Borey Residents Submit Petitions Over housing Dispute"
        },
        {
            "id": 103,
            "title": "Local New Year Revelers Fuel Tourism Revival Hopes"
        },
        {
            "id": 104,
            "title": "Irrawaddy Dolphin Calf Born on New Year’s Eve"
        },
        {
            "id": 105,
            "title": "Cambodia Detects First Omicron Community Case"
        },
        {
            "id": 106,
            "title": "Cambodia’s Female Coder"
        },
        {
            "id": 107,
            "title": "Interior Design Students On the Rise"
        },
        {
            "id": 108,
            "title": "Cambodia Bids a Fond Farewell to HeroRAT Magawa"
        },
        {
            "id": 109,
            "title": "Japan Gives $185m Loan for Covid Recovery"
        },
        {
            "id": 110,
            "title": "How STEM Is Modernizing Cambodia’s Education System"
        },
        {
            "id": 111,
            "title": "Farmers Battle Against Rising Costs"
        },
        {
            "id": 112,
            "title": "Women Take up Technical Roles"
        },
        {
            "id": 113,
            "title": "From Phnom Penh with Love"
        },
        {
            "id": 114,
            "title": "Artists Given Platform to Shine"
        },
        {
            "id": 115,
            "title": "Multi-million Dollar Loan to Boost Education"
        },
        {
            "id": 116,
            "title": "The City Sweepers"
        },
        {
            "id": 117,
            "title": "Omicron Casts Shadow Over Cambodia Tourism Revival"
        },
        {
            "id": 118,
            "title": "Cambodian Rap Song Urges Action Over Climate Change"
        },
        {
            "id": 119,
            "title": "Cambodia's ACLEDA Unveils Expansion Plans to Vietnam"
        },
        {
            "id": 120,
            "title": "Wing Bank Invests $2m in New Airport"
        },
        {
            "id": 121,
            "title": "Pork and Chicken Price Hike"
        },
        {
            "id": 122,
            "title": "AmCam Event Celebrates International Ties"
        },
        {
            "id": 123,
            "title": "Rice Export Receives Boost as Tariffs Are Scrapped"
        },
        {
            "id": 124,
            "title": "Stray Animals Given Fresh Lease of Life"
        },
        {
            "id": 125,
            "title": "Traditional Cambodian Silk Weaving at Threat"
        },
        {
            "id": 126,
            "title": "World Bank Outlines Steps to Boost Cambodia’s Economy"
        },
        {
            "id": 127,
            "title": "Incentives Needed for Electric Vehicles to Zoom in Cambodia"
        },
        {
            "id": 129,
            "title": "Sastra Film cofounder’s high hopes for Cambodia’s burgeoning  film industry"
        },
        {
            "id": 130,
            "title": "Student Loan Scheme Unveiled for Digital Education"
        },
        {
            "id": 131,
            "title": "Innovation Platform Aims To Boost Cambodia's Fishery Sector"
        },
        {
            "id": 132,
            "title": "Cambodian Bank’s Shares Sky-rocket As Stock Buyout is Revealed"
        },
        {
            "id": 133,
            "title": "Indigenous children face hurdles in access to education during the pandemic"
        },
        {
            "id": 134,
            "title": "ACLEDA Bank Announces Record 2021 Profits"
        },
        {
            "id": 135,
            "title": "Internet Provider Given Seven Days to Settle Debt"
        },
        {
            "id": 136,
            "title": "Ministry Pledges $100m to Help Covid-hit Sectors Grow"
        },
        {
            "id": 137,
            "title": "ADB Gives $95m Loan to Boost Cambodia’s Vaccination Campaign"
        },
        {
            "id": 138,
            "title": "Hike in Profits Reported on Cambodian Stock Exchange"
        },
        {
            "id": 139,
            "title": "Calls for Cambodia to Invest More in Digital Education"
        },
        {
            "id": 140,
            "title": "PRASAC Microfinance Announces Asset Portfolio of $4.3 billion"
        },
        {
            "id": 141,
            "title": "Race to grow startup ecosystem and founders in Cambodia"
        },
        {
            "id": 142,
            "title": "Opennet Banned from Sourcing New Customers Over $6m Debt Row"
        },
        {
            "id": 143,
            "title": "Trash for Cash Scheme Aims To Clean Up Cambodian Coast"
        },
        {
            "id": 144,
            "title": "Sihanoukville Autonomous Port Records Profit Growth"
        },
        {
            "id": 145,
            "title": "Women Head 61% of Cambodia’s Businesses"
        },
        {
            "id": 146,
            "title": "A $15m Cash Injection Aims to Bridge Cambodia’s Digital Skills Gap"
        },
        {
            "id": 147,
            "title": "Female Entrepreneur Beats the Odds to Launch Mobile Home Business"
        },
        {
            "id": 148,
            "title": "Female Innovators are Transforming Cambodian Agriculture"
        },
        {
            "id": 149,
            "title": "Technology Company Aims to Elevate and Digitalize Community"
        },
        {
            "id": 150,
            "title": "Anti-snare Campaign Launched to Protect Cambodia’s Wildlife"
        },
        {
            "id": 151,
            "title": "Cambodia Lags in Digital Literacy"
        },
        {
            "id": 152,
            "title": "First Post-Covid Commercial Flight Lands in Sihanoukville"
        },
        {
            "id": 153,
            "title": "Financial Literacy Education is Key to Manage Household Finances"
        },
        {
            "id": 154,
            "title": "Mediators Essential to Resolve Business Disputes"
        },
        {
            "id": 155,
            "title": "Cambodia’s Female Entrepreneurs Given Platform to Grow"
        },
        {
            "id": 156,
            "title": "Students to be Offered Loans to Continue University Studies"
        },
        {
            "id": 157,
            "title": "Cambodia’s Health Sector Receives $113m Cash Boost"
        },
        {
            "id": 158,
            "title": "Social Enterprise Upcycles Waste to Keep It from Landfill"
        },
        {
            "id": 159,
            "title": "Investing in Cambodia’s future: when startups meet angel investors"
        },
        {
            "id": 160,
            "title": "Must-have apps for everyday life in Cambodia"
        },
        {
            "id": 161,
            "title": "Cool contact-less payment with Acleda PayBand"
        },
        {
            "id": 162,
            "title": "Education Key to Post-Pandemic Economic Growth"
        },
        {
            "id": 163,
            "title": "Bunong Homeland Added to Global Watchlist"
        },
        {
            "id": 164,
            "title": "From Family Salt Farm to International Business"
        },
        {
            "id": 165,
            "title": "$5m Fund to Stimulate Cambodia’s Startup Scene"
        },
        {
            "id": 167,
            "title": "Innovative Eco-solution Helps Clean Cambodia’s Sewage"
        },
        {
            "id": 169,
            "title": "BLOG - Cambodia’s Early Warning System 1294: An Adaptable Technology Promoting Safety"
        },
        {
            "id": 170,
            "title": "BMC Startup Program Sows the Seeds for Entrepreneurs"
        },
        {
            "id": 171,
            "title": "Cambodia Unveils Electric Vehicle Roadmap"
        },
        {
            "id": 172,
            "title": "Turning Plastics into Profits"
        },
        {
            "id": 173,
            "title": "Project Aims to Elevate Cambodia’s Digital Literacy"
        },
        {
            "id": 174,
            "title": "Fears War in Ukraine Will Spark Inflation Increase"
        },
        {
            "id": 175,
            "title": "Support Loan Scheme Launched to Strengthen Agricultural Sector"
        },
        {
            "id": 176,
            "title": "Cambodia Academy of Digital Technology’s Graduates Ready for New Journey"
        },
        {
            "id": 177,
            "title": "Even Without Internet in Mobile Phones, Users Can Still Use ACLEDA Mobile"
        },
        {
            "id": 178,
            "title": "Acleda ATMs and cool features"
        },
        {
            "id": 179,
            "title": "Login to Acleda Mobile while wearing a mask"
        },
        {
            "id": 180,
            "title": "Project Aims to Modernize Cambodian Farming"
        },
        {
            "id": 181,
            "title": "Welcome to Cambodia’s metaverse"
        },
        {
            "id": 182,
            "title": "Cash Transfer Scheme Neglects Nation’s Urban and Service Workers"
        },
        {
            "id": 183,
            "title": "ABA Bank Announces $212.02m Profits"
        },
        {
            "id": 184,
            "title": "ACLEDA Bank Opens Inaugural Branch in Aoral District"
        },
        {
            "id": 185,
            "title": "Two Programs Join Hands to Push Digital Literacy Outside Phnom Penh"
        },
        {
            "id": 186,
            "title": "Cambodia ICT Camp Aims to Elevate Digital Security and Data Journalism"
        },
        {
            "id": 187,
            "title": "New Book to Help Foreigners Navigate Cambodia’s Business Sector"
        },
        {
            "id": 188,
            "title": "Digital Platform Aims to Eradicate Khmer Illiteracy"
        },
        {
            "id": 189,
            "title": "E-market Platform Aims to Promote Cambodian Produce"
        },
        {
            "id": 190,
            "title": "Life-saving App Aims to Reduce Cancer Deaths in Cambodia"
        },
        {
            "id": 191,
            "title": "ACLEDA: Payment via QR Scans Skyrocket during Khmer New Year"
        },
        {
            "id": 192,
            "title": "Role Model Raises Cambodia’s Female Tech Startup Scene"
        },
        {
            "id": 193,
            "title": "Siemens Partners with CADT to Provide World-Class Tech Training"
        },
        {
            "id": 194,
            "title": "Online shopping made easy with Acleda Mobile"
        },
        {
            "id": 195,
            "title": "Edtechs Boost Cambodia's Education in Post-Pandemic World"
        },
        {
            "id": 196,
            "title": "Earth Day Fashion Show Throws Spotlight on Endangered Species"
        },
        {
            "id": 197,
            "title": "Investment in ACLEDA Bank Breaks Stock Exchange Record"
        },
        {
            "id": 198,
            "title": "Cambodia-Japan Business Matching to Attract More Investors"
        },
        {
            "id": 199,
            "title": "Coffee Shops Promote Reading and Art in Cambodia"
        },
        {
            "id": 200,
            "title": "Call for Vehicle Owners to Pay Import Duties"
        },
        {
            "id": 201,
            "title": "Construction Starts on $1.5b Kampot Port"
        },
        {
            "id": 202,
            "title": "Home-grown Travel App Promotes Tourism Across Cambodia"
        },
        {
            "id": 203,
            "title": "Telehealth Startup Aims to Revolutionise Healthcare in Cambodia"
        },
        {
            "id": 204,
            "title": "Compost City Startup Turns Food Wastes into Fertilizers"
        },
        {
            "id": 205,
            "title": "Coworking Space in the Capital Is Being Reinvented"
        },
        {
            "id": 206,
            "title": "ACLEDA Celebrates Being Cambodia’s First Bank to Provide Custodian Services"
        },
        {
            "id": 207,
            "title": "Educational Startup To Equip Low-income Kids With Digital Devices"
        },
        {
            "id": 208,
            "title": "Homegrown Fertilizer to Boost Cambodia’s Crops"
        },
        {
            "id": 209,
            "title": "Demand for Media Production Skills on the Rise"
        },
        {
            "id": 210,
            "title": "INTERVIEW - Female Coder Problem-solves Through Apps"
        },
        {
            "id": 211,
            "title": "Coconut-based Social Enterprise Ravaged by Covid"
        },
        {
            "id": 212,
            "title": "Film Festival’s Return Aims to Revitalize Cinema Industry"
        },
        {
            "id": 213,
            "title": "Rising Living Costs Hit Informal Workers Hard"
        },
        {
            "id": 214,
            "title": "Social Media Campaign Raises Awareness About Energy Efficiency"
        },
        {
            "id": 215,
            "title": "RESYNC Hybrid Storytelling Program Aims to Unify Peace and Art"
        },
        {
            "id": 216,
            "title": "Space to Spark Creativity in the Cambodian Capital"
        },
        {
            "id": 217,
            "title": "Start-Up Helps Indigenous Women Access Education"
        },
        {
            "id": 218,
            "title": "Vietnam Airlines Sells Stake in Cambodia Angkor Air"
        },
        {
            "id": 219,
            "title": "Cambodia Exports 283,675 Tons of Rice in Five Months"
        },
        {
            "id": 220,
            "title": "ICT Camp Throws Spotlight on Open Data and Data Journalism"
        },
        {
            "id": 221,
            "title": "Pioneering Products to be Unveiled at Annual TVET Event"
        },
        {
            "id": 222,
            "title": "Improved Capacity and Investment Key to Develop Cambodian Media"
        },
        {
            "id": 223,
            "title": "Ukraine Invasion Stalls Cambodia’s Economic Growth"
        },
        {
            "id": 224,
            "title": "ACLEDA Partners with Forest Interactive to Offer Digital Payments"
        },
        {
            "id": 225,
            "title": "Covid Robot Finds New Role in School"
        },
        {
            "id": 226,
            "title": "Partnership Gives ACLEDA Customers Access to Global Transactions"
        },
        {
            "id": 227,
            "title": "Inaugural Coding and Developer Camp Aims to Grow Cambodia’s Sector"
        },
        {
            "id": 228,
            "title": "A Tech Company is Preparing Cambodia for the Digital Revolution"
        },
        {
            "id": 229,
            "title": "Students As Young as Seven Study Coding in Cambodia"
        },
        {
            "id": 230,
            "title": "Technology Being Used as a Tool to Drive Economic Growth"
        },
        {
            "id": 231,
            "title": "DHL Singapore Adds 80 Electric Vehicles to Fleet"
        },
        {
            "id": 232,
            "title": "Disabled Farmers Fight for Equality"
        },
        {
            "id": 233,
            "title": "Cambodia’s Annual ICT Camp Celebrates Successful Start"
        },
        {
            "id": 234,
            "title": "ACLEDA and Western Union Unite to Offer International Transfers"
        },
        {
            "id": 235,
            "title": "Cambodia’s Cybercrime Law Remains Under Review"
        },
        {
            "id": 236,
            "title": "Expert Urges Caution when Shopping Online"
        },
        {
            "id": 237,
            "title": "Digital Security for Children is Key"
        },
        {
            "id": 238,
            "title": "Expert Raises Concerns About the Risk of Fake News"
        },
        {
            "id": 239,
            "title": "Partnership Aims to Increase Cambodia’s Digital Education"
        },
        {
            "id": 240,
            "title": "Social Education Platform Focuses on Learning for Cambodian Youth"
        },
        {
            "id": 241,
            "title": "Value of Data Visualization in the Media"
        },
        {
            "id": 242,
            "title": "Recovering Cambodian Economy Hit by Global Fuel Crisis"
        },
        {
            "id": 243,
            "title": "Deal to Strengthen Cambodia’s Digital Assets Sector"
        },
        {
            "id": 244,
            "title": "Tech Startups in Cambodia are Growing"
        },
        {
            "id": 245,
            "title": "Government Collects $490 Million Taxes in June"
        },
        {
            "id": 246,
            "title": "Easy Payments Via ACLEDA App"
        },
        {
            "id": 247,
            "title": "Social Business Provides Jobs for Cambodia’s Women Knitters"
        },
        {
            "id": 248,
            "title": "Dollarized Economy Essential for Foreign Investment"
        },
        {
            "id": 249,
            "title": "Pension Scheme Extended to the Private Sector"
        },
        {
            "id": 250,
            "title": "US Plans to Strengthen Regional Ties"
        },
        {
            "id": 251,
            "title": "Cambodia’s Untapped Tourism Potential"
        },
        {
            "id": 252,
            "title": "China to Increase Rice Imports from Cambodia"
        },
        {
            "id": 253,
            "title": "Online Businesses Fine Warning"
        },
        {
            "id": 255,
            "title": "EDC Predicted to Lose $100m"
        },
        {
            "id": 256,
            "title": "Coastal SMEs Eligible to Apply for $2m Fund"
        },
        {
            "id": 257,
            "title": "Cambodia’s Pension Scheme to Start in October"
        },
        {
            "id": 258,
            "title": "$2m Funding for Coastal Entrepreneurs Officially Launches"
        },
        {
            "id": 259,
            "title": "Order for Right-hand Drive Vehicles to Switch Steering Side Scrapped"
        },
        {
            "id": 260,
            "title": "Dreams to Create Home-grown Cambodian Cheese"
        },
        {
            "id": 261,
            "title": "Binance Deal puts Cambodian Cryptocurrency Regulations on the Horizon"
        },
        {
            "id": 262,
            "title": "Sihanoukville Struggles Due to Exodus of Chinese Investors"
        },
        {
            "id": 263,
            "title": "Non-state Chinese Media Expands to Preah Sihanouk"
        },
        {
            "id": 264,
            "title": "Fuel to Fall By 0.14 Cents"
        },
        {
            "id": 265,
            "title": "ACLEDA Securities Most Traded Value on Cambodian Stock Exchange"
        },
        {
            "id": 266,
            "title": "Cambodia’s Coast and Capital-based Businesses Hit Hard by Covid-19"
        },
        {
            "id": 267,
            "title": "US State Visit Aims to Bolster Bilateral Ties"
        },
        {
            "id": 268,
            "title": "Traffic Accidents Trigger Vehicle Ban On the $2b Phnom Penh- Sihanoukville Expressway"
        },
        {
            "id": 269,
            "title": "New Mondulkiri Airport Stalled"
        },
        {
            "id": 270,
            "title": "Cambodian Minister Urges US to Renew Duty-free Export Program"
        },
        {
            "id": 271,
            "title": "Phnom Penh Port Reports Bumper $19m Revenue"
        },
        {
            "id": 272,
            "title": "US “Closely” Monitoring Cambodian Online Scam Operations"
        },
        {
            "id": 273,
            "title": "Stolen Cambodian Antiquities Return From the US"
        },
        {
            "id": 274,
            "title": "Accelerator Program Launched for Agritech Startups"
        },
        {
            "id": 275,
            "title": "Cambodia’s Tourism Industry Faces Fresh Challenges"
        },
        {
            "id": 276,
            "title": "Cambodian Authorities Pledge to Keep Migrant Workers in Thailand Safe"
        },
        {
            "id": 277,
            "title": "Euro Fall Against the Dollar to Trigger Demand in Export Decrease"
        },
        {
            "id": 278,
            "title": "Cambodian Women Entrepreneurs Share Their Success"
        },
        {
            "id": 279,
            "title": "INTERVIEW - Author Addresses Issues on the Tonle Sap Lake"
        },
        {
            "id": 280,
            "title": "Gold Prices Tumble Amid Uncertain Global Markets"
        },
        {
            "id": 281,
            "title": "INTERVIEW-First Indigenous Female in Tech Education"
        },
        {
            "id": 282,
            "title": "Thai Tech Giant Invests $3m in Cambodian Media Platform"
        },
        {
            "id": 283,
            "title": "Khmer Rouge Documents Preserved for Future Generations"
        },
        {
            "id": 284,
            "title": "Counting the Cost of Cambodia’s Hydropower Dams"
        },
        {
            "id": 285,
            "title": "Call for Female Founders to Enter Annual Global Competition"
        },
        {
            "id": 286,
            "title": "Swire Pacific Strikes Deal to Buy Cambodian Coca Cola Bottling Plant"
        },
        {
            "id": 287,
            "title": "Female Entrepreneur Crowned Advocate of the Year at International Awards"
        },
        {
            "id": 288,
            "title": "More than 700 Fuel Stations Con Customers"
        },
        {
            "id": 289,
            "title": "National News Reaches Arabic Market"
        },
        {
            "id": 290,
            "title": "Cambodia to Export Longan to China"
        },
        {
            "id": 291,
            "title": "Cambodians Cautioned to Shield Against Pegasus Cyber-Attacks"
        },
        {
            "id": 292,
            "title": "Road Tolls Implemented for PP-SHV Expressway"
        },
        {
            "id": 293,
            "title": "Rice Exports Earn Cambodia $600m in Six months"
        },
        {
            "id": 294,
            "title": "Orussey Market Vendors Protest Over Rental Price Hike"
        },
        {
            "id": 295,
            "title": "Government Subsidies of $31m Given to Female Workers"
        },
        {
            "id": 296,
            "title": "Female Business Owner’s Challenges to Overcome Covid"
        },
        {
            "id": 297,
            "title": "Microsoft Teams Recovering After Outage"
        },
        {
            "id": 298,
            "title": "In Conversation with Cambodia’s ‘Longan Wine’ Maker, Vouch Thuch"
        },
        {
            "id": 299,
            "title": "Almost $2b in Taxes Collected in Six Months"
        },
        {
            "id": 300,
            "title": "Fuel Prices Fall a Further $0.11 Cents"
        },
        {
            "id": 301,
            "title": "Price of Durian Stabilizes After 50 Percent Fall"
        },
        {
            "id": 302,
            "title": "Thai Crypto Exchange Zipmex Halts Withdrawals"
        },
        {
            "id": 303,
            "title": "Cambodian Female Achieves Dream of Working at Google"
        },
        {
            "id": 304,
            "title": "NBC Predicts Fall in Inflation"
        },
        {
            "id": 306,
            "title": "Cambodian Agriculture Faces Raft of Challenges to Grow"
        },
        {
            "id": 307,
            "title": "Falling Crocodile Prices Leave Farmers Fighting for Livelihoods"
        },
        {
            "id": 308,
            "title": "Startups Vs SMEs: Exit Strategy is Key"
        },
        {
            "id": 309,
            "title": "$1.5b Real Estate Project Launches in Phnom Penh"
        },
        {
            "id": 310,
            "title": "Gold Prices in Cambodia Rise"
        },
        {
            "id": 311,
            "title": "Orussey Market Vendors Prepare to File Petition With Authorities"
        },
        {
            "id": 312,
            "title": "China Launches $44.4b Real Estate Fund"
        },
        {
            "id": 313,
            "title": "Chinese Imports to Cambodia Total $5.37b in Six Months"
        },
        {
            "id": 314,
            "title": "Is Cambodia’s mobile payment built for ASEAN integration?"
        },
        {
            "id": 315,
            "title": "Ministry Bans Use of Signal Boosters"
        },
        {
            "id": 316,
            "title": "Satellite Internet Set to Enter Cambodia in 2023"
        },
        {
            "id": 317,
            "title": "Cambodian Startups Invited to Expand Digital Skills with Amazon"
        },
        {
            "id": 318,
            "title": "Is Elon Musk’s Speedy Satellite Internet Workable in Southeast Asia?"
        },
        {
            "id": 319,
            "title": "Cambodia Crowned the Region’s Saddest Country"
        },
        {
            "id": 320,
            "title": "Sihanoukville Official Urges Solution to Incomplete Construction"
        },
        {
            "id": 321,
            "title": "Top US, Chinese and Russian Officials to Attend ASEAN Ministers' Meeting"
        },
        {
            "id": 322,
            "title": "Talented musician Bosba Panh Urges West to Give Cambodians “Space” to Share their Rich Culture Globally"
        },
        {
            "id": 323,
            "title": "Sihanoukville SEZ Exports $1.3b in Six months"
        },
        {
            "id": 324,
            "title": "Mobile App for Cambodians to Lodge Public Service Complaints Launches"
        },
        {
            "id": 325,
            "title": "Authorities Kick-start Tax Inspections in Phnom Penh"
        },
        {
            "id": 326,
            "title": "Authorities to Inspect Foreigners’ Accommodation"
        },
        {
            "id": 327,
            "title": "Heavy Investment Essential for Cambodia's Rice Exports to Remain Competitive"
        },
        {
            "id": 328,
            "title": "Mandatory Vehicle Insurance to be Implemented"
        },
        {
            "id": 329,
            "title": "Founder’s Story: Chim Poly is Restyling Cambodia’s Barbershop Experience"
        },
        {
            "id": 330,
            "title": "Bridging the Startup Gap Between Cambodia and Israel"
        },
        {
            "id": 331,
            "title": "Online Lenders Target Cambodian Women in Extortion Scam"
        },
        {
            "id": 332,
            "title": "AgriTech Firm Azaylla Receives Investment from Singapore"
        },
        {
            "id": 333,
            "title": "Rising Inflation Rates Destroy Cambodian Livelihoods"
        },
        {
            "id": 334,
            "title": "Initiative Launched to Link Local Agro-food Producers with Foreign Investors"
        },
        {
            "id": 335,
            "title": "Deadline for Removal of Advertising on Battambang Buildings Lapses"
        },
        {
            "id": 336,
            "title": "Is Cambodia Ready for Smart Cities and 5G?"
        },
        {
            "id": 337,
            "title": "Cambodian Tycoon Writes Will Ahead of Treatment in Singapore"
        },
        {
            "id": 338,
            "title": "Cambodia’s Oil Dreams Remain Afloat"
        },
        {
            "id": 339,
            "title": "Cambodian Debt Stands at $9.81b"
        },
        {
            "id": 340,
            "title": "China Turns to Music as Relations with Cambodia Sweeten"
        },
        {
            "id": 341,
            "title": "Indonesia Joins Fight Against Online Scams and Human Trafficking"
        },
        {
            "id": 342,
            "title": "ASEAN Leaders Gather in Phnom Penh"
        },
        {
            "id": 343,
            "title": "Cambodian Delegation of Entrepreneurs to Visit Israel"
        },
        {
            "id": 344,
            "title": "Cambodia’s Tourism Ministry Unveils Plans to Attract More Tourists"
        },
        {
            "id": 345,
            "title": "Paid Internship Scheme Aims to Recruit 1,000 Students"
        },
        {
            "id": 346,
            "title": "Singapore Investors to Help Reboot Cambodia’s Economy"
        },
        {
            "id": 347,
            "title": "Cambodia-China Bilateral Trade Hits $11b"
        },
        {
            "id": 348,
            "title": "ACE Marks 30 Years of Education in Cambodia"
        },
        {
            "id": 349,
            "title": "Cambodia’s Expats to Enjoy Free Access to Angkor"
        },
        {
            "id": 350,
            "title": "Exclusive Contracts Between Boreys and Internet Service Providers Banned"
        },
        {
            "id": 351,
            "title": "US Foreign Secretary Unveils $25m Food Safety Project"
        },
        {
            "id": 352,
            "title": "City Sweep Evicts Homeless from Battambang’s Streets"
        },
        {
            "id": 353,
            "title": "A $200m Japanese Loan to Upscale Sihanoukville Port"
        },
        {
            "id": 354,
            "title": "National Domain Name Brings $10m in Revenue"
        },
        {
            "id": 355,
            "title": "Rescuing Cambodia’s Feline Friends"
        },
        {
            "id": 356,
            "title": "Angkor’s Elephants Find A New Home"
        },
        {
            "id": 357,
            "title": "Iconic Raffles in Siem Reap Celebrates 90th Anniversary"
        },
        {
            "id": 358,
            "title": "Bamboo Airways Connects Siem Reap with Hanoi"
        },
        {
            "id": 359,
            "title": "Japan to Loan $383m to Develop Sihanoukville Port"
        },
        {
            "id": 360,
            "title": "Drivers Warned to Carry Documents"
        },
        {
            "id": 361,
            "title": "Garment Workers Minimum Wage to be Reviewed"
        },
        {
            "id": 362,
            "title": "Creating A Multi-Million Dollar Rice Enterprise"
        },
        {
            "id": 363,
            "title": "US and Cambodia Launch $25m Program to Bolster Agriculture"
        },
        {
            "id": 364,
            "title": "Looted Antiquities to be Returned to Cambodia"
        },
        {
            "id": 365,
            "title": "Stolen Crude Oil to Be Returned to Cambodia"
        },
        {
            "id": 366,
            "title": "Orussey Market's Stall Prices Remain the Same"
        },
        {
            "id": 367,
            "title": "Royal Group SEZ Increases Exports by $492.7m"
        },
        {
            "id": 368,
            "title": "Phnom Penh to Host Global SME Finance Forum"
        },
        {
            "id": 369,
            "title": "Australian Miners Find Gold in Mondulkiri"
        },
        {
            "id": 370,
            "title": "Grant Offered to Export Entrepreneurs"
        },
        {
            "id": 371,
            "title": "Construction Sector Totaled $5.3b in 2021"
        },
        {
            "id": 372,
            "title": "Cambodia-Thailand Bilateral Trade Totals $3.85b"
        },
        {
            "id": 373,
            "title": "AMCHAM Visits the US to Strengthen Ties"
        },
        {
            "id": 374,
            "title": "Collective Rice Brands Aim to Boost Exports"
        },
        {
            "id": 375,
            "title": "Summit to Tackle Cambodia’s Solid Waste Issues"
        },
        {
            "id": 376,
            "title": "Clean Water Startup Receives $300,000 Cash Injection"
        },
        {
            "id": 377,
            "title": "Fines Waived for Tour Guides with Expired Licenses"
        },
        {
            "id": 378,
            "title": "Appeal for Funds to Save Community Radio Station"
        },
        {
            "id": 379,
            "title": "Cambodia Ready to Export Longan to China"
        },
        {
            "id": 380,
            "title": "Chinese Hungry Ghost Festival Marked in Phnom Penh"
        },
        {
            "id": 381,
            "title": "Cambodia Bike Exports Total $500m in Seven Months"
        },
        {
            "id": 382,
            "title": "From Village Singer to Salon Star"
        },
        {
            "id": 383,
            "title": "International Hotel Brand TRIBE Opens in Phnom Penh"
        },
        {
            "id": 384,
            "title": "ACLEDA Bank Marks 10-Year Partnership with Japanese shareholder SMBC"
        },
        {
            "id": 385,
            "title": "Amazon to Train Cloud Experts in Cambodia"
        },
        {
            "id": 386,
            "title": "Citizen Participation and Innovation Key to Sustainable Cities"
        },
        {
            "id": 387,
            "title": "New Book to Help Cambodia Navigate Cyberspace"
        },
        {
            "id": 388,
            "title": "Orussey Market Vendors File Petition with PM"
        },
        {
            "id": 390,
            "title": "Minimum Wage Negotiations for Garment Workers Begin"
        },
        {
            "id": 391,
            "title": "Sala and PSE Partner to Deliver Improved Education in Cambodia"
        },
        {
            "id": 392,
            "title": "Exhibition Uses Art to Heal Females Rescued From Sex Trafficking"
        },
        {
            "id": 393,
            "title": "Big Data’s Potential to Aid Post-Pandemic Recovery"
        },
        {
            "id": 394,
            "title": "Right-Hand Vehicle Owners Warned to Pay Taxes"
        },
        {
            "id": 395,
            "title": "Limited US-Cambodia Relations Pushing Phnom Penh to Beijing"
        },
        {
            "id": 396,
            "title": "Teachers to Receive Pay Hike to 1.5m Riel by 2023"
        },
        {
            "id": 397,
            "title": "How Cambodia Built Its Digital Data Exchange"
        },
        {
            "id": 398,
            "title": "Decision for Free Expat Access to Angkor Awaits"
        },
        {
            "id": 399,
            "title": "Troubled Community Radio Station Relocates to Home"
        },
        {
            "id": 400,
            "title": "Innovative Cookery School Puts Mothers Back in Work"
        },
        {
            "id": 401,
            "title": "Cambodian Crickets Being Prepped for Export"
        },
        {
            "id": 402,
            "title": "PM Orders Petitioning Factory Workers be Paid"
        },
        {
            "id": 403,
            "title": "PM Reassures Regional Food Insecurity is No Issue"
        },
        {
            "id": 404,
            "title": "Tech Crucial for Agriculture to Thrive"
        },
        {
            "id": 405,
            "title": "Public Financial Reports from Listed Companies Key for Investment"
        },
        {
            "id": 406,
            "title": "Entrepreneurs Advised to Register to Reap Benefits"
        },
        {
            "id": 407,
            "title": "Illegal Structures in Angkor to be Torn Down"
        },
        {
            "id": 408,
            "title": "Cambodia’s SMEs Battle String of Challenges"
        },
        {
            "id": 409,
            "title": "Khoding Hero Program Trains Svay Rieng Students to Join Digital Workforce"
        },
        {
            "id": 410,
            "title": "ABA Announces Record $130.6m Profits in Six Months"
        },
        {
            "id": 411,
            "title": "Safety Fears Raised as Citizens Cut Fencing to Cross $2b Highway"
        },
        {
            "id": 412,
            "title": "AR Technology’s Potential to Stimulate Tourism"
        },
        {
            "id": 413,
            "title": "Clampdown on Illegal Foreign Workers Begins"
        },
        {
            "id": 414,
            "title": "Improving Education Through Toys"
        },
        {
            "id": 415,
            "title": "Journey From Full-Time Employee to YouTube Star"
        },
        {
            "id": 416,
            "title": "Trash Collectors Key to Cambodia’s Recycling"
        },
        {
            "id": 417,
            "title": "New Book Depicts ACLEDA Bank’s Historic Milestones"
        },
        {
            "id": 418,
            "title": "Licenses Issued for 47 Casinos and Seven Lotteries"
        },
        {
            "id": 419,
            "title": "Pipe Leak Triggers Water Cut in Phnom Penh"
        },
        {
            "id": 420,
            "title": "Transforming Education One Library at A Time"
        },
        {
            "id": 421,
            "title": "Lon Nol Information Minister Chhang Song Dies"
        },
        {
            "id": 422,
            "title": "Singaporean Fintech Firm Enters Cambodia to Target Banking Sector"
        },
        {
            "id": 423,
            "title": "Selling Organic Local Produce to Help Farmers Grow"
        },
        {
            "id": 424,
            "title": "Collaboration is Key to Cambodian Education’s Pandemic Recovery"
        },
        {
            "id": 425,
            "title": "Talks to Export Rice to Bangladesh Begin"
        },
        {
            "id": 426,
            "title": "Cap on Civil Servant Recruits to Save National Budget"
        },
        {
            "id": 427,
            "title": "Applications Open for National Awards that Celebrate Digital Innovation"
        },
        {
            "id": 428,
            "title": "China and Cambodia to Create Modern Agriculture Master Plan"
        },
        {
            "id": 429,
            "title": "MoU Signed to Strengthen Cambodia’s SME Sector"
        },
        {
            "id": 430,
            "title": "Sihanoukville Port Records $18.9m Profits in Six Months"
        },
        {
            "id": 431,
            "title": "$1.6m Fund to Promote Inclusivity in Agriculture"
        },
        {
            "id": 432,
            "title": "Sale of Asbestos-infected Talc Temporarily Halted"
        },
        {
            "id": 433,
            "title": "Unions Push for Minimum Wage of $215 for Garment Workers"
        },
        {
            "id": 434,
            "title": "Almost 700 Families Voluntarily Move from Angkor"
        },
        {
            "id": 435,
            "title": "Vietnam is Ripe to Produce APAC’s Next Tech Unicorn"
        },
        {
            "id": 436,
            "title": "Emotional Reunion for World’s Loneliest Elephant and Rescuer"
        },
        {
            "id": 437,
            "title": "Authorities Reclaim 65,000 Hectares of Flooded Forest"
        },
        {
            "id": 438,
            "title": "Government Gears up to Issue $300m Bonds"
        },
        {
            "id": 439,
            "title": "Clampdown on Illegal Online Lending"
        },
        {
            "id": 440,
            "title": "Cambodian Farmers to Benefit from $500,000 Fund"
        },
        {
            "id": 441,
            "title": "$1.2b Pumped into Construction Sector in Six months"
        },
        {
            "id": 442,
            "title": "AI Technology Helps Garment Factories Eliminate Deforestation"
        },
        {
            "id": 443,
            "title": "Event to Bolster Business Between ASEAN Entrepreneurs"
        },
        {
            "id": 444,
            "title": "Almost 870 Foreigners Rescued from Human Trafficking Scams"
        },
        {
            "id": 445,
            "title": "Reshaping Eco-friendly Shopping"
        },
        {
            "id": 446,
            "title": "Cambodia’s Agricultural Sector Immune to Impacts of Covid"
        },
        {
            "id": 447,
            "title": "“Rare Treasure” Mekong Review Folds"
        },
        {
            "id": 448,
            "title": "Tech Startup Making Access to Finance Easier"
        },
        {
            "id": 449,
            "title": "Angkor Evictees Continue to Look for New Land"
        },
        {
            "id": 450,
            "title": "Digital Transformation Essential for Economic Resilience"
        },
        {
            "id": 451,
            "title": "Cambodia Pepper Exports Fall by 70 Percent"
        },
        {
            "id": 452,
            "title": "New Fishways Provide Lifeline to Aqua Life in Pursat"
        },
        {
            "id": 453,
            "title": "The Trials and Tribulations of the Donut King’s Life"
        },
        {
            "id": 454,
            "title": "Waste Remains Huge Concern Across Cambodia"
        },
        {
            "id": 455,
            "title": "Strengthening STEM Education Is A Priority"
        },
        {
            "id": 456,
            "title": "Investor Map Launched to Identify Opportunities"
        },
        {
            "id": 457,
            "title": "Cambodia to Start Exporting Corn to China"
        },
        {
            "id": 458,
            "title": "Future Plans to Create Subways to Ease Capital’s Traffic Unveiled"
        },
        {
            "id": 459,
            "title": "Unions Push for Minimum Garment Workers Wage of $213"
        },
        {
            "id": 460,
            "title": "Minister Calls for US to Reinstate Trade Deal"
        },
        {
            "id": 461,
            "title": "Program Aims​​ To Assess Learning Levels in Education"
        },
        {
            "id": 462,
            "title": "Cambodia’s Sustainable Investment Opportunities"
        },
        {
            "id": 463,
            "title": "China Donates 150 Vehicles for ASEAN Defense Ministers’ Meeting"
        },
        {
            "id": 464,
            "title": "Miss Grand Organisers Apologise For “Sexy” Attire"
        },
        {
            "id": 465,
            "title": "Measures Rolled Out to Strengthen Cambodia’s Cultural and Creative Industries"
        },
        {
            "id": 466,
            "title": "Cambodia’s Stock Market Share Prices Explained"
        },
        {
            "id": 467,
            "title": "Expats Can Enjoy Free Entry to Angkor for One Year"
        },
        {
            "id": 468,
            "title": "7-Eleven Marks One Year in Cambodia"
        },
        {
            "id": 469,
            "title": "Israel to Investigate Introducing New Agricultural Technologies"
        },
        {
            "id": 470,
            "title": "Cambodia Earns $11.6m From Carbon Credit Sales"
        },
        {
            "id": 471,
            "title": "Inspiring Cambodian Women Leaders One Interview At A Time"
        },
        {
            "id": 472,
            "title": "Adopting Technology is Key to Develop Health Sector"
        },
        {
            "id": 473,
            "title": "Why Cambodia should aim for centaur startups, instead of unicorns"
        },
        {
            "id": 474,
            "title": "EuroCham Pushes for Switch to Solar and Zero Capacity Charges"
        },
        {
            "id": 475,
            "title": "Digitalization Key for Women SMEs to Thrive"
        },
        {
            "id": 477,
            "title": "Cambodian Finswimmer Scoops Four Medals"
        },
        {
            "id": 478,
            "title": "Turning Banana Trees into Handmade Handicrafts"
        },
        {
            "id": 481,
            "title": "Creating a Digital Community Around Food Menus"
        },
        {
            "id": 482,
            "title": "Lab Tests Reveal Asbestos-contaminated Talc is Safe"
        },
        {
            "id": 483,
            "title": "Contract Farming in Cambodia Increases"
        },
        {
            "id": 484,
            "title": "Rising Flight Prices Impact Tourism Rebound"
        },
        {
            "id": 485,
            "title": "ASEAN Unites To Stamp Out Looting of Antiquities"
        },
        {
            "id": 486,
            "title": "Plastic Campaign Aims to Promote Tourism Industry"
        },
        {
            "id": 487,
            "title": "Plans to Empower Women in Work"
        },
        {
            "id": 488,
            "title": "Hotline Proved Key in Curbing Covid Spread"
        },
        {
            "id": 489,
            "title": "Poipet Education Center Provides Schooling to Vulnerable Kids"
        },
        {
            "id": 490,
            "title": "Monsoon Rains Flood 45,362 Hectares of Paddies"
        },
        {
            "id": 491,
            "title": "Helpline Launched to Aid Entrapped Chinese Workers"
        },
        {
            "id": 492,
            "title": "Fears Raised Over Cybercrime Draft Law"
        },
        {
            "id": 493,
            "title": "Committee to Oversee New Airport Agreements"
        },
        {
            "id": 494,
            "title": "Royal Railways on Track to Receive $10m Bond"
        },
        {
            "id": 495,
            "title": "Impact of Covid-19 on Cambodia’s Informal Sector"
        },
        {
            "id": 496,
            "title": "Is the Metaverse the Next Big Business Opportunity in Cambodia?"
        },
        {
            "id": 497,
            "title": "Moon Festival Festivities in Cambodia"
        },
        {
            "id": 499,
            "title": "False Advertisers Issued Warning"
        },
        {
            "id": 500,
            "title": "Toyota Invests $36.7m to Set Up Operations in Cambodia"
        },
        {
            "id": 501,
            "title": "Inflation Predicted to Fall Below Five Percent"
        },
        {
            "id": 502,
            "title": "Health and Economic Concerns May Hamper Pchum Ben Celebrations"
        },
        {
            "id": 503,
            "title": "$3.4m Donated to Tackle Child Wasting"
        },
        {
            "id": 504,
            "title": "Startup CamSEED to Stop Sowing Seeds"
        },
        {
            "id": 505,
            "title": "PM Calls for Free Transport During Pchum Ben"
        },
        {
            "id": 506,
            "title": "Expansion of KHR Cross-Border Payments by QR Code in ASEAN"
        },
        {
            "id": 507,
            "title": "Defying the Odds to Follow Her Dreams"
        },
        {
            "id": 508,
            "title": "New Care Center Opens for Kids with Disabilities in Prey Veng"
        },
        {
            "id": 509,
            "title": "Education Ministry Orders School Shut Down for ASEAN Summit"
        },
        {
            "id": 510,
            "title": "PM Orders Cards be Issued to Relocated Families from Angkor"
        },
        {
            "id": 511,
            "title": "Cambodia Given Green Light to Export Longan to China"
        },
        {
            "id": 512,
            "title": "Guilt of Eating Packaged Food with Plastic Leads to Eco-Restaurant"
        },
        {
            "id": 513,
            "title": "PATHMAZING to Lead Management and Fundraising for SEA Games 2023"
        },
        {
            "id": 514,
            "title": "The Hunt for the Holy Grail in Israel to Build Cambodia As a Startup Kingdom"
        },
        {
            "id": 515,
            "title": "Push to Introduce RCEP Independent Secretariat"
        },
        {
            "id": 516,
            "title": "Meeting to Determine Final Decision on Minimum Wages Set"
        },
        {
            "id": 517,
            "title": "Government Urged to Introduce Pension Schemes for Elderly"
        },
        {
            "id": 518,
            "title": "Urgent Need to Address Debt Caused by MFIs"
        },
        {
            "id": 519,
            "title": "New Digital Habits and Trends in Southeast Asia Revealed"
        },
        {
            "id": 520,
            "title": "Water Festival Celebrations in the Capital Scrapped"
        },
        {
            "id": 521,
            "title": "Plea to Push Further Integration of ASEAN Power Grids"
        },
        {
            "id": 522,
            "title": "$1m Initiative to Push Sustainable Tourism"
        },
        {
            "id": 523,
            "title": "Construction of Cambodia’s first Vaccine Plant Slated to Start"
        },
        {
            "id": 524,
            "title": "Threatened Mekong Review’s Legacy Lives On"
        },
        {
            "id": 525,
            "title": "Thai Startup Growth Hampered by Limited Tech Talent"
        },
        {
            "id": 526,
            "title": "ACLEDA Installs QR Codes at Pagodas for Pchum Ben Offerings"
        },
        {
            "id": 527,
            "title": "FinTech Workshop Responds to Growth in Digital Economy"
        },
        {
            "id": 528,
            "title": "Creating Eco-Friendly Urban Spaces"
        },
        {
            "id": 529,
            "title": "Electric Vehicle Charge Stations Key to Drive Nationwide Switch"
        },
        {
            "id": 530,
            "title": "$58m Program Launched to Support Agriculture and Infrastructure"
        },
        {
            "id": 531,
            "title": "Fermented Kampot Pepper Crowned ‘Oscar’ of Food"
        },
        {
            "id": 532,
            "title": "Finance Sector Rejects Study Claiming MFIs Cause Over-indebtedness"
        },
        {
            "id": 533,
            "title": "Crackdown on Illegal Gambling Rolled Out"
        },
        {
            "id": 534,
            "title": "Free Train Travel During Pchum Ben"
        },
        {
            "id": 535,
            "title": "Liger School Students to Launch Cambodian Economy Book"
        },
        {
            "id": 536,
            "title": "Deadline for Right-hand Drive Tax Payments Looms"
        },
        {
            "id": 537,
            "title": "MoU Signed to Push Financial Literacy"
        },
        {
            "id": 538,
            "title": "Minister of Interior Urges Continued Crackdown on Crime in Sihanoukville"
        },
        {
            "id": 539,
            "title": "China Donates Military Equipment and Vehicles to Cambodia"
        },
        {
            "id": 540,
            "title": "Accredited Lab To Boost Food Safety Nationwide"
        },
        {
            "id": 541,
            "title": "PM Prepares for Official Visits to US, Cuba and Japan"
        },
        {
            "id": 542,
            "title": "Phnom Penh to Host Inaugural Tech Expo"
        },
        {
            "id": 543,
            "title": "Inflation to Peak this Year Before Showing Signs of Decline"
        },
        {
            "id": 544,
            "title": "Minimum Wage Increased to $200"
        },
        {
            "id": 545,
            "title": "PP-SHV Expressway to Officially Open in November"
        },
        {
            "id": 546,
            "title": "Global Finance Forum Aims to Support Cambodia’s SMEs"
        },
        {
            "id": 547,
            "title": "Plans Discussed to Grant Thais Easy Access to the Temples"
        },
        {
            "id": 548,
            "title": "France to Provide Financial Aid for Cambodia’s Post-Pandemic Recovery"
        },
        {
            "id": 549,
            "title": "The Inspiring Life of a Cambodian Drag Queen"
        },
        {
            "id": 550,
            "title": "Gold Exports Fall as Imports Rise"
        },
        {
            "id": 551,
            "title": "ACLEDA Scoops Award for Aiding Cambodian SMEs"
        },
        {
            "id": 552,
            "title": "Citizens Cash in on Free Train Travel"
        },
        {
            "id": 553,
            "title": "Soil Microbe Technology Poised to Help Farmers Grow"
        },
        {
            "id": 554,
            "title": "Heavy Floods Threaten Thousands of Siem Reap Families"
        },
        {
            "id": 555,
            "title": "ACLEDA Crowned SME Financier of the Year"
        },
        {
            "id": 556,
            "title": "Search for 23 Chinese passengers from Capsized Sihanoukville Boat"
        },
        {
            "id": 557,
            "title": "Tough Crackdown Causes Chinese to Flee Sihanoukville"
        },
        {
            "id": 558,
            "title": "More than 2,000 Expats Apply for Free Angkor Pass"
        },
        {
            "id": 559,
            "title": "Teenage Students Launch Book on Cambodian Economics"
        },
        {
            "id": 560,
            "title": "Six Cambodian Women Shortlisted for Women of Future Awards"
        },
        {
            "id": 561,
            "title": "ACLEDA Bank Sponsors 9th Global SME Finance Forum 2022"
        },
        {
            "id": 562,
            "title": "Forum Promotes Development of Cambodia’s Soft Skills"
        },
        {
            "id": 563,
            "title": "Forum on Tax Updates A Key Event for Businesses"
        },
        {
            "id": 564,
            "title": "Iconic Cuisine Wat Damnak to Reopen in Siem Reap"
        },
        {
            "id": 565,
            "title": "World Bank Projects 4.5 percent Economic Growth for 2022"
        },
        {
            "id": 566,
            "title": "Sihanoukville Development “Challenges”"
        },
        {
            "id": 567,
            "title": "Capsized Boat Passengers Suspected Illegal Immigrants"
        },
        {
            "id": 568,
            "title": "ACLEDA Mobile App Upgrade Brings More Benefits"
        },
        {
            "id": 569,
            "title": "Two Million Tourists to Visit Cambodia in 2022"
        },
        {
            "id": 570,
            "title": "ADB $15b Project Aims to Ease Regional Food Insecurity"
        },
        {
            "id": 571,
            "title": "Tax Law Slated to be Passed by End of Year"
        },
        {
            "id": 572,
            "title": "Ministry Issues Warning Over Facebook Payments"
        },
        {
            "id": 573,
            "title": "Heavy Floods Kill 13 and Threaten Lives Across Five Provinces"
        },
        {
            "id": 574,
            "title": "The Building Blocks to Secure Angel Investment"
        },
        {
            "id": 575,
            "title": "The “People’s Healer” Awarded Asia’s Nobel Peace Prize"
        },
        {
            "id": 576,
            "title": "Bitcoin Incentive Launched by Ride-Hailing Service TADA"
        },
        {
            "id": 577,
            "title": "Gambling A Front for Human Trafficking, Says PM"
        },
        {
            "id": 578,
            "title": "Cambodia to Receive 70% of Stolen Oil Revenue"
        },
        {
            "id": 579,
            "title": "Korea Ratifies Free Trade Agreement"
        },
        {
            "id": 580,
            "title": "ACLEDA Customers Can Pay in riel via QR Scan in Thailand"
        },
        {
            "id": 581,
            "title": "Income Tax Set for 2023"
        },
        {
            "id": 582,
            "title": "​Capsized Boat was Smuggling Chinese"
        },
        {
            "id": 583,
            "title": "Plans Lodged for $17m Tourism Project on Koh Tbal"
        },
        {
            "id": 584,
            "title": "Call for Tourism Workers to Return to Industry"
        },
        {
            "id": 585,
            "title": "Eco-Laundry Ball Aims to Tackle Environmental Issues"
        },
        {
            "id": 586,
            "title": "Workers Set to Lose Eight Public Holidays in 2023"
        },
        {
            "id": 587,
            "title": "Credit Bureau Marks 10 Years of Service"
        },
        {
            "id": 588,
            "title": "Video Competition Aims to Raise Awareness About Breast Cancer"
        },
        {
            "id": 589,
            "title": "Improving Cambodia’s Startup Investment Ecosystem"
        },
        {
            "id": 590,
            "title": "Income Tax Revenue Hits $250m A Month"
        },
        {
            "id": 591,
            "title": "Green Financing Key to Cambodia’s Energy Transition"
        },
        {
            "id": 592,
            "title": "Vaccination Certificate on Arrival Scrapped"
        },
        {
            "id": 593,
            "title": "Cambodian-American Footballer’s Pride Playing for the Nation"
        },
        {
            "id": 594,
            "title": "MoU to Drive Sustainable Development Goals"
        },
        {
            "id": 595,
            "title": "Asian Banks Urged to Uphold Rights in Agricultural Sector"
        },
        {
            "id": 596,
            "title": "500 Underprivileged Kids to Access Digital Math Tool"
        },
        {
            "id": 597,
            "title": "Handcrafting Jewellery from Waste Horns"
        },
        {
            "id": 598,
            "title": "How to Become A Data Scientist"
        },
        {
            "id": 599,
            "title": "BRED Bank Appoints New Boss"
        },
        {
            "id": 600,
            "title": "Prizes Worth $3,500 Unclaimed in TADA Bitcoin Initiative"
        },
        {
            "id": 601,
            "title": "Right-hand Drive Vehicle Owners Given More Time to Pay Taxes"
        },
        {
            "id": 602,
            "title": "Siem Reap E-bus Initiative Moves Forward"
        },
        {
            "id": 603,
            "title": "Competition Calls for Innovators to Design Technology to Monitor the Mekong"
        },
        {
            "id": 604,
            "title": "Singaporean Volunteers Pledge to Help Villagers Access Clean Water"
        },
        {
            "id": 605,
            "title": "Broadcasters Warned Not to Illegally Screen FIFA World Cup"
        },
        {
            "id": 606,
            "title": "Cambodia Tech Expo Expected to Attract 60,000 Attendees"
        },
        {
            "id": 607,
            "title": "PM Calls for Calm from Villagers Protesting Against Eviction"
        },
        {
            "id": 608,
            "title": "Call for Startups to Pitch for up to $250,000 Investment"
        },
        {
            "id": 609,
            "title": "Psychotherapist Advocates Speaking Out to Improve Mental Well-being"
        },
        {
            "id": 610,
            "title": "No Forced Evictions for Preah Dak Residents"
        },
        {
            "id": 611,
            "title": "Cash Scheme to Decrease Inflation Burden"
        },
        {
            "id": 612,
            "title": "Phnom Penh Photo Festival Returns to Capital"
        },
        {
            "id": 613,
            "title": "Using Art to Grow Wings and “Escape the Chaos”"
        },
        {
            "id": 614,
            "title": "Average Small Business Loan Amount Rises by 250%"
        },
        {
            "id": 615,
            "title": "Investment Framework Key for SME Sector's Covid-19 Recovery"
        },
        {
            "id": 616,
            "title": "New Agriculture Minister Nominated"
        },
        {
            "id": 617,
            "title": "AI and e-Governance Key to Access Information in Digital World"
        },
        {
            "id": 618,
            "title": "Branded Watches Designed for Leaders Attending ASEAN Regional Summit"
        },
        {
            "id": 619,
            "title": "Legal Experts Essential for Startups"
        },
        {
            "id": 620,
            "title": "Strong Leadership Key to Cope with Crises"
        },
        {
            "id": 621,
            "title": "NagaCorp Hits Refinancing Risk"
        },
        {
            "id": 622,
            "title": "Wat Bo Village Voted World's Third Coolest Neighbourhood"
        },
        {
            "id": 623,
            "title": "Better Factories Cambodia to Continue For Additional Five Years"
        },
        {
            "id": 624,
            "title": "Suspended Tourism Workers to Receive Benefits"
        },
        {
            "id": 625,
            "title": "Garment Exports Drop"
        },
        {
            "id": 626,
            "title": "E-waste Solution Scoops Award at Regional Data Competition"
        },
        {
            "id": 627,
            "title": "Fake Rabies Vaccine Banned"
        },
        {
            "id": 628,
            "title": "Cambodia and Cyprus Strengthen Ties"
        },
        {
            "id": 629,
            "title": "Khmer Language Schools to be Set Up in Countries of Migrant Workers"
        },
        {
            "id": 630,
            "title": "Cambodia to Host Mekong Tourism Forum 2023"
        },
        {
            "id": 631,
            "title": "Mental Well-being is Key to a Healthy Life"
        },
        {
            "id": 632,
            "title": "Students Die in Tragic Ferry Sinking"
        },
        {
            "id": 633,
            "title": "New Agriculture Minister Approved"
        },
        {
            "id": 634,
            "title": "Campaign Aims to Safeguard the Rainforest"
        },
        {
            "id": 635,
            "title": "Cambodian and Thai Firms Jointly Launch Robotic Tech Business"
        },
        {
            "id": 636,
            "title": "Tourism to Bump Up Cambodia’s GDP to 6.2% in 2023"
        },
        {
            "id": 637,
            "title": "Streetside Korean Fried Chicken Store to Online Wholesale Grocery Platform"
        },
        {
            "id": 638,
            "title": "Tributes Paid to Capsized Ferry Victims"
        },
        {
            "id": 639,
            "title": "Official Countdown to SEA Games Begins"
        },
        {
            "id": 640,
            "title": "Keeping Social Enterprises Alive During Covid"
        },
        {
            "id": 641,
            "title": "MFIs Urged to Help Ease Flood Victims' Financial Burden"
        },
        {
            "id": 642,
            "title": "Phnom Penh port sees 30% jump in Jan-Sept container throughput"
        },
        {
            "id": 643,
            "title": "Davy Chou Film Selected to Represent Cambodia at Oscars"
        },
        {
            "id": 644,
            "title": "AI Tool to Map Cambodia's Vulnerabilities"
        },
        {
            "id": 645,
            "title": "Lack of Agricultural Experience No Issue for New Minister"
        },
        {
            "id": 646,
            "title": "Golden Tree Sets Green Bond Coupon Rate at 7%"
        },
        {
            "id": 647,
            "title": "MFIs Agree to Loan Repayment Relief for Borrowers Hit by Flooding"
        },
        {
            "id": 648,
            "title": "Reviving Cambodian Weaving"
        },
        {
            "id": 649,
            "title": "Blockchain Technology Explained"
        },
        {
            "id": 650,
            "title": "Khmer Enterprise to Double Startup and SME Investment to $10M"
        },
        {
            "id": 651,
            "title": "Charismatic Cambodian Cyclo Star in ‘City of Ghosts’ Dies"
        },
        {
            "id": 652,
            "title": "Deal Signed to Stimulate Rice Exports to Mongolia"
        },
        {
            "id": 653,
            "title": "MoU to Boost Aviation Ties with Timor-Leste"
        },
        {
            "id": 654,
            "title": "Summit Aims to Bridge the Digital Divide"
        },
        {
            "id": 655,
            "title": "Angkor Period Asura Statue Found at Angkor Thom"
        },
        {
            "id": 656,
            "title": "CSX Event Aims to Increase Investment in the Stock Market"
        },
        {
            "id": 657,
            "title": "FMO Proposes Pumping $15m into Cambodian MFI"
        },
        {
            "id": 658,
            "title": "CSX Launches App and Online Platform to Ease Trading"
        },
        {
            "id": 659,
            "title": "Relocated Angkor Residents to Receive Free Electricity Connection"
        },
        {
            "id": 660,
            "title": "Visitors Needed to Keep Community Ecotourism Project Afloat"
        },
        {
            "id": 661,
            "title": "PillTech Raises Half a Million Dollars to Transform Cambodian Pharmacies"
        },
        {
            "id": 662,
            "title": "Kampot Fishermen Struggle to Survive Amid Declining Fish Stocks"
        },
        {
            "id": 663,
            "title": "A Total of 263 Foreigners Deported for Crimes"
        },
        {
            "id": 664,
            "title": "Proud Moment As Cambodian Plants National Flag at Everest in Memory of Brother"
        },
        {
            "id": 665,
            "title": "Ferry Captain of 50 Years Passes on Baton to his Son"
        },
        {
            "id": 666,
            "title": "Rapper VannDa’s ‘Time to Rise’ Reaches 100m YouTube Views"
        },
        {
            "id": 667,
            "title": "Cambodian and UAE Relations Set to Strengthen"
        },
        {
            "id": 668,
            "title": "Chinese Investors Discuss Developing Koh Kong Electric Car Plant"
        },
        {
            "id": 669,
            "title": "Fundraiser for Revered Chapei Performer Master Kong Nay"
        },
        {
            "id": 670,
            "title": "Using Art as a Voice"
        },
        {
            "id": 671,
            "title": "CRF to Serve UAE Rice Market"
        },
        {
            "id": 672,
            "title": "Turning Cambodia Into A Tech-Ready Country"
        },
        {
            "id": 673,
            "title": "Summit Promotes Inclusive Business Across ASEAN"
        },
        {
            "id": 674,
            "title": "Urgent Call for Delayed Works on Roads 2 and 22 to Finish"
        },
        {
            "id": 675,
            "title": "Cambodia Starts Exporting Longans to China"
        },
        {
            "id": 676,
            "title": "Pandemic Pushes Public Mistrust in the Media"
        },
        {
            "id": 677,
            "title": "Sovereign Bonds’ Slow Take-Off Prompts MEF To Revise Up Coupon Rates, Yield"
        },
        {
            "id": 678,
            "title": "A STEM Classroom Is Creating Cambodia’s Future Scientists"
        },
        {
            "id": 679,
            "title": "Magazine Sparks Cambodian Kids’ Curiosity and Creativity"
        },
        {
            "id": 680,
            "title": "$9.6 Billion 2023 National Budget Approved"
        },
        {
            "id": 681,
            "title": "Silent Forests: Post-pandemic Wildlife Consumption Threatens Human and Forest Health"
        },
        {
            "id": 682,
            "title": "Land Disputes Settled Through Mediation"
        },
        {
            "id": 683,
            "title": "WWII Movie Filmed in Cambodia Hits Cinemas"
        },
        {
            "id": 684,
            "title": "Royal Railway Lists Bonds on CSX to Raise $10m for Rail Upgrades"
        },
        {
            "id": 685,
            "title": "Increasing Domestic Agriculture Key to Preventing Food Inflation"
        },
        {
            "id": 686,
            "title": "Improved ICT Training Key to Prep Cambodia for the Digital Revolution"
        },
        {
            "id": 687,
            "title": "Meta Cambodia Launches Digital Economy Portal"
        },
        {
            "id": 688,
            "title": "Government to Borrow 1,700m SDR in 2023"
        },
        {
            "id": 689,
            "title": "Metfone’s YouTube Channel Hits 1M Subscribers"
        },
        {
            "id": 690,
            "title": "Digital Skills and Education Ecosystem Key to Digital Transformation"
        },
        {
            "id": 691,
            "title": "Local Rice Seed Production Plans Discussed"
        },
        {
            "id": 692,
            "title": "PP-SHV Expressway Road Tolls Implemented"
        },
        {
            "id": 693,
            "title": "Draft 2023 Financial Law Responds to Post-Pandemic Economy"
        },
        {
            "id": 694,
            "title": "Ukraine Remains ASEAN Food Security Guarantor"
        },
        {
            "id": 695,
            "title": "RCEP to Boost Trade by $40B"
        },
        {
            "id": 696,
            "title": "ADB and EDC Sign Mandate to Further Cambodia’s Renewable Energy Goals"
        },
        {
            "id": 697,
            "title": "Biz Fair to Attract 500,000 Visitors to Cambodia’s Coast"
        },
        {
            "id": 698,
            "title": "Push to Promote “Five Countries, One Destination” Tourism Campaign"
        },
        {
            "id": 699,
            "title": "700 MW Coal-Fired Powerplant Starts Operations"
        },
        {
            "id": 700,
            "title": "Cambodia and Kuwait Strengthen Trade Ties"
        },
        {
            "id": 701,
            "title": "Australia Offers $51m to Aid Cambodia’s Covid-19 Recovery"
        },
        {
            "id": 702,
            "title": "Food Security and Safety Key Components for Development"
        },
        {
            "id": 703,
            "title": "VC Pledges $1m to Early-Stage Cambodian Startups"
        },
        {
            "id": 704,
            "title": "DBDE extends losses in 3Q, gross loans up"
        },
        {
            "id": 705,
            "title": "Silent Forests: To Save Wildlife in Cambodia, Conservationists Attempt a ‘Last Ditch Effort’"
        },
        {
            "id": 706,
            "title": "Single Mum Builds Advertising Agency from Scratch"
        },
        {
            "id": 707,
            "title": "Creating Powerful YouTube Content"
        },
        {
            "id": 708,
            "title": "Officials Arrive in Phnom Penh for ASEAN Summit"
        },
        {
            "id": 709,
            "title": "Cafe Brings A Taste of Japan to Siem Reap"
        },
        {
            "id": 710,
            "title": "Cambodia’s Tourism Rebound Hampered by Global Crises"
        },
        {
            "id": 711,
            "title": "China’s Slow Economy Puts a Strain on Cambodian Exports"
        },
        {
            "id": 712,
            "title": "Hun Sen Calls for Increased Vietnamese Investment"
        },
        {
            "id": 713,
            "title": "Ministry of Post and Telecommunications Signs Strategic Cooperation Agreement with Viettel Cambodia"
        },
        {
            "id": 714,
            "title": "China Signs 18 Agreements to Aid Cambodia"
        },
        {
            "id": 715,
            "title": "Work on PP-Bavet Expressway to Start in 2023"
        },
        {
            "id": 716,
            "title": "Minister Calls on Philippines to Increase Cambodian Rice Imports"
        },
        {
            "id": 717,
            "title": "Running Alternative Media Platforms"
        },
        {
            "id": 718,
            "title": "Vietnam’s Prime Minister Visits Metfone"
        },
        {
            "id": 719,
            "title": "Building Bridges Between Cambodia and Israel"
        },
        {
            "id": 720,
            "title": "Online Platform Elevates Cambodia’s Fintech Sector"
        },
        {
            "id": 721,
            "title": "Metfone Helping to Build Cambodia’s Digital Society"
        },
        {
            "id": 722,
            "title": "Cambodian Open-Source Platform Wins Prestigious Award in Singapore"
        },
        {
            "id": 723,
            "title": "Muslim World League Promotes Peace Between Religions"
        },
        {
            "id": 724,
            "title": "ASEAN to Admit Timor-Leste as 11th Member"
        },
        {
            "id": 725,
            "title": "Ministers Discuss Cambodia-Thailand Border Projects"
        },
        {
            "id": 726,
            "title": "China and Cambodia’s PMs Exchange Praise at ASEAN-China Summit"
        },
        {
            "id": 727,
            "title": "Myanmar No Show At ASEAN Summits as Russian Foreign Minister Attends"
        },
        {
            "id": 728,
            "title": "ADB Pledges $100b to Tackle Regional Climate Change"
        },
        {
            "id": 729,
            "title": "US President Joe Biden Arrives in Cambodia for ASEAN Summit"
        },
        {
            "id": 730,
            "title": "Building Bridges Between Cambodia and Israel (Last Part)"
        },
        {
            "id": 731,
            "title": "US President Joe Biden Meets With Hun Sen"
        },
        {
            "id": 732,
            "title": "ASEAN Summits Come to A Successful End"
        },
        {
            "id": 733,
            "title": "IMF Chief Fears Sleepwalking into Poorer, Less Secure World"
        },
        {
            "id": 734,
            "title": "Joint Venture Plans to Grow Cambodia’s Blockchain Ecosystem"
        },
        {
            "id": 735,
            "title": "First Cambodia Tech Expo Drives Digital Transformation"
        },
        {
            "id": 736,
            "title": "International Fund Targets Raising $1b to Fund Independent Media"
        },
        {
            "id": 737,
            "title": "Watches Gifted to ASEAN Summit Leaders Cost $20,000 Each"
        },
        {
            "id": 738,
            "title": "EdTech Startup Aims to Modernize Education"
        },
        {
            "id": 739,
            "title": "Higher Finance Costs Drags Pestech into the Red in 1Q"
        },
        {
            "id": 740,
            "title": "Sihanoukville Port Q3 Results Delayed to Dec 5 This Year"
        },
        {
            "id": 741,
            "title": "ASEAN Youth Leader Program Boosts Cross-Border Collaboration"
        },
        {
            "id": 742,
            "title": "PM Tests Positive for Covid at G20 Summit in Bali"
        },
        {
            "id": 743,
            "title": "Experts Gather at CTX 2022 to Drive Cambodia’s Electronics and Automotive Sectors"
        },
        {
            "id": 744,
            "title": "ACLEDA’s Q3 Net Profit Hits $50m on Higher Interest Income, Fees"
        },
        {
            "id": 745,
            "title": "First Food Safety Certification Launched for Fish Industry"
        },
        {
            "id": 746,
            "title": "PPSP Returns to the Black on Robust Land Sales in Q3"
        },
        {
            "id": 747,
            "title": "Moody’s Revises Cambodia’s Outlook to Negative from Stable"
        },
        {
            "id": 748,
            "title": "State-owned PPWSA’s Net Profits More Than Halve in Q3"
        },
        {
            "id": 749,
            "title": "PM Concerned for ASEAN Summit World Leaders After Testing Covid-19 Positive"
        },
        {
            "id": 750,
            "title": "Awareness and Training Key to Toughen Up Cambodia’s Cyberspace"
        },
        {
            "id": 751,
            "title": "60-MW Solar Park Pumps Power into the Grid"
        },
        {
            "id": 752,
            "title": "Call for Farmers Impacted by Rice Price Fall to Contact Ministry"
        },
        {
            "id": 753,
            "title": "Cambodian Banks Face Higher NPL in 2023"
        },
        {
            "id": 754,
            "title": "Bond Issuer Prasac’s 3Q Earnings Snagged by Higher Impairment Allowance"
        },
        {
            "id": 755,
            "title": "ASEAN Summit Global Leaders Covid-Free"
        },
        {
            "id": 756,
            "title": "Phnom Penh’s Potential to Evolve into a Smart City"
        },
        {
            "id": 757,
            "title": "Warning Issued to Landlords Charging Residents for Internet"
        },
        {
            "id": 758,
            "title": "Cambodian Rice Crowned World’s Best"
        },
        {
            "id": 759,
            "title": "Cambodia’s Startup Investment Gap"
        },
        {
            "id": 760,
            "title": "Ministry Pledges to Bring Justice to Officials Accused of Smuggling Monkeys into US"
        },
        {
            "id": 761,
            "title": "Two Tourism Training Schools to Open"
        },
        {
            "id": 762,
            "title": "Phare Wins Guinness Title for Longest Circus Act"
        },
        {
            "id": 763,
            "title": "Tap Strives to Digitalize Cambodia’s Taxi Booking Landscape"
        },
        {
            "id": 764,
            "title": "Gaelic Football Team to Compete in World Games in Ireland"
        },
        {
            "id": 765,
            "title": "An Adventure in Laos"
        },
        {
            "id": 766,
            "title": "Cambodian Officials Charged With Wildlife Trafficking, a ‘Wake-up Call’ for Global Monkey Trade"
        },
        {
            "id": 767,
            "title": "Cambodian Health Startups Head to Switzerland to Build Business"
        },
        {
            "id": 768,
            "title": "Sand Boat Slams into Chroy Changva Bridge"
        },
        {
            "id": 769,
            "title": "Monkey Farm Denies Allegations of Smuggling Macaques into US"
        },
        {
            "id": 770,
            "title": "Work Ongoing to Fully Restore ACLEDA Mobile App"
        },
        {
            "id": 771,
            "title": "A Record Number of Lesser Adjutant Nests Found"
        },
        {
            "id": 772,
            "title": "Explainer: How to Receive and Send Money in Cambodia"
        },
        {
            "id": 773,
            "title": "ACLEDA Bank Says App Back Online"
        },
        {
            "id": 774,
            "title": "$10m Fund to Buy Rice from Struggling Farmers"
        },
        {
            "id": 775,
            "title": "Opening Ceremony for National Games and Paralympic Games Goes Off to a Bang"
        },
        {
            "id": 776,
            "title": "Public Transport as a Catalyst for an Egalitarian Society and Sustainable Future"
        },
        {
            "id": 777,
            "title": "Tech Academy Developing Cambodia’s Future Digital Workforce"
        },
        {
            "id": 778,
            "title": "Buddhist Teaching is a Tool for Mental Health Support in Cambodia"
        },
        {
            "id": 779,
            "title": "Chaktomuk Short Film Festival Welcomes Rise in Entries"
        },
        {
            "id": 780,
            "title": "Inflation Rises to 7.4 Percent"
        },
        {
            "id": 781,
            "title": "GDP Growth to Shrink to 4.9% as Poverty Rate Inches Up"
        },
        {
            "id": 782,
            "title": "Kampot Mining Concession Open to Bidders"
        },
        {
            "id": 783,
            "title": "SHE Investments’ Women Digipreneurs Event to Upskill and Empower Businesswomen"
        },
        {
            "id": 784,
            "title": "Making Green Finance A Reality"
        },
        {
            "id": 785,
            "title": "Cambodia to Export 25,000 Tons of Rice to Bangladesh"
        },
        {
            "id": 786,
            "title": "Community Kindergarten Helping to End Poverty Cycle"
        },
        {
            "id": 787,
            "title": "China Sets Hygiene Requirements for Cambodian Pepper"
        },
        {
            "id": 788,
            "title": "YouTube Lifts Ban on Monetizing in Cambodia"
        },
        {
            "id": 789,
            "title": "Conference Throws Spotlight on Key Role of Banks"
        },
        {
            "id": 790,
            "title": "Wat Bo Pocket Guide Promotes Area to Visitors"
        },
        {
            "id": 791,
            "title": "Blockchain Technology: A Key Enabler of Future Smart  Supply Chain Management"
        },
        {
            "id": 792,
            "title": "Swire Coca-Cola Opens Bottle Business in Cambodia"
        },
        {
            "id": 793,
            "title": "Responsible Business Hub to Elevate Due Diligence"
        },
        {
            "id": 794,
            "title": "Clamp Down on Unlicensed Tourism Businesses"
        },
        {
            "id": 795,
            "title": "Innovative TEDxRUPP Returns"
        },
        {
            "id": 796,
            "title": "Kampong Thom Math Teachers to Learn New Skills from Master Trainers"
        },
        {
            "id": 797,
            "title": "Meeting Vietnam’s Cotu Mountain People"
        },
        {
            "id": 798,
            "title": "Coffee Shop Atmosphere and Flavor are Major Draws for Customers"
        },
        {
            "id": 799,
            "title": "Cambodia’s Poverty Rate Halved in 2019"
        },
        {
            "id": 800,
            "title": "Cambodia Book Fair Promotes Reading Culture"
        },
        {
            "id": 801,
            "title": "PillTech Co-Founder Shares Inspiration Behind His Startup"
        },
        {
            "id": 802,
            "title": "Chinese EV Manufacturer to Install 200 Charging Stations"
        },
        {
            "id": 803,
            "title": "GDP Leader Defects, Calls on PM to Resolve Farmers’ Issues"
        },
        {
            "id": 804,
            "title": "Acleda Shares Hold Court on CSX Index Despite Low Valuations"
        },
        {
            "id": 805,
            "title": "Protected Royal Turtle Found with Severe Fractured Skull"
        },
        {
            "id": 806,
            "title": "Cambodia Signs Deal to Export Renewable Energy to Singapore"
        },
        {
            "id": 807,
            "title": "Third Expressway to Connect Phnom Penh and Siem Reap"
        },
        {
            "id": 808,
            "title": "Inaugural Responsible Business Hub Opens"
        },
        {
            "id": 809,
            "title": "UNDP Donates 31 Electric Vehicles to Ministry"
        },
        {
            "id": 810,
            "title": "Cambodia Urges Japan to Reinstate Direct Flights"
        },
        {
            "id": 811,
            "title": "Graphic Novel Chronicles Life of ‘Golden Era’ Popstar"
        },
        {
            "id": 812,
            "title": "Limit to be Set on Age of Imported Cars"
        },
        {
            "id": 813,
            "title": "Connection Sits at the Heart of Mental Health"
        },
        {
            "id": 814,
            "title": "Kun Lbokator Inscribed on UNESCO World Heritage List"
        },
        {
            "id": 815,
            "title": "Cambodia and Kuwait to Strengthen Bilateral Ties"
        },
        {
            "id": 816,
            "title": "Nieman Fellow Seeks to Inspire Female Peers"
        },
        {
            "id": 817,
            "title": "National and Paralympic Games Close with a Bang"
        },
        {
            "id": 818,
            "title": "Japan Pledges $4.1m to Build Two Rice Warehouses"
        },
        {
            "id": 819,
            "title": "Japanese Manufacturer to Explore Opening Solar-Powered Factory in Cambodia"
        },
        {
            "id": 820,
            "title": "Cambodia Wins Lawsuit Opposing European Commission Revoking Rice Import Tariffs"
        },
        {
            "id": 821,
            "title": "Sihanoukville Port’s Net Profit up 10.5% in Q3"
        },
        {
            "id": 822,
            "title": "Online Portal Aims to Stamp Out “Revenge Porn” in Cambodia"
        },
        {
            "id": 823,
            "title": "“People’s Healer” Receives Asia’s Most Prestigious Award for Mental Health Services"
        },
        {
            "id": 824,
            "title": "Tight Measures to Prevent Cheating as Students Start Exams"
        },
        {
            "id": 825,
            "title": "DJ Nana: “I Don’t Have A Plan”"
        },
        {
            "id": 826,
            "title": "Tackling Cambodia’s Environmental Health Risks"
        },
        {
            "id": 827,
            "title": "Rising Costs Impact Daily Life"
        },
        {
            "id": 828,
            "title": "Cash Support Program Launched for Vulnerable"
        },
        {
            "id": 829,
            "title": "Commercial Advertisement Sub-Decree Issued"
        },
        {
            "id": 830,
            "title": "Business Model Competition Opens to Uni Students"
        },
        {
            "id": 831,
            "title": "CamDX Awarded Open Source Adaptation"
        },
        {
            "id": 832,
            "title": "$100m Funding Provided to SMEs in 2023"
        },
        {
            "id": 833,
            "title": "Call for Clamp Down on Vape Sales on Social Media"
        },
        {
            "id": 834,
            "title": "ADB Approves $50m Loan"
        },
        {
            "id": 835,
            "title": "ACLEDA’s Dividend Likely Up to 50 Percent of Profits for FY’22, Highest So Far"
        },
        {
            "id": 836,
            "title": "Cambodia’s Startup Ecosystem Praised at Angkor 500 Turn Up"
        },
        {
            "id": 837,
            "title": "The Role of Fintech in Future Cities"
        },
        {
            "id": 838,
            "title": "Cambodia Hosts YSEALI Summit"
        },
        {
            "id": 839,
            "title": "Launching Cambodia’s Credit Bureau"
        },
        {
            "id": 840,
            "title": "$2.1m EU Grants to Promote Democracy and Freedom of Expression"
        },
        {
            "id": 841,
            "title": "AEON Mall 3 Gears Up To Open"
        },
        {
            "id": 842,
            "title": "Handicrafts Incubator Throws Lifeline to Struggling Artisans"
        },
        {
            "id": 843,
            "title": "ADB Approves $73m Funding to Strengthen Marine Fisheries"
        },
        {
            "id": 844,
            "title": "Cambodia Digital Awards Celebrates Pioneering Tech Landscape"
        },
        {
            "id": 845,
            "title": "Economic Growth to Increase to 5.2 percent in 2023"
        },
        {
            "id": 846,
            "title": "South Korea to Approve $1.5b Loan to Develop Cambodia’s Economy"
        },
        {
            "id": 847,
            "title": "Mandatory Drug Test in New Traffic Law"
        },
        {
            "id": 848,
            "title": "Innovative Pilot Project Produces Rice Husk Briquettes"
        },
        {
            "id": 849,
            "title": "What’s Holding Back Companies From Listing on CSX?"
        },
        {
            "id": 850,
            "title": "Sea Festival Draws Crowds to Sihanoukville"
        },
        {
            "id": 851,
            "title": "Youth Voices Matter! Project Comes to an End"
        },
        {
            "id": 852,
            "title": "BarCamp DigiTech Heads to Battambang"
        },
        {
            "id": 853,
            "title": "AirAsia Cambodia to Take Off to Expand ASEAN Market Share"
        },
        {
            "id": 854,
            "title": "Parenting in Modern Times"
        },
        {
            "id": 855,
            "title": "Destination Mekong Summit to Strengthen Tourism Recovery"
        },
        {
            "id": 856,
            "title": "How Investors Decide to Invest in Start-ups"
        },
        {
            "id": 857,
            "title": "Dutch Lender Allegedly Failed to Conduct Due Diligence on Investments"
        },
        {
            "id": 858,
            "title": "Three National Heritage Monk Residence Demolished"
        },
        {
            "id": 859,
            "title": "ADB Pours in $62.9m to Improve Farmers’ Livelihoods"
        },
        {
            "id": 860,
            "title": "Port Ops Push Up PPAP’s Revenue by 22 Percent"
        },
        {
            "id": 861,
            "title": "PM Bans Energy Price Hike"
        },
        {
            "id": 862,
            "title": "BarCamp DigiTech Calls for Northwestern SMEs and Students to Adapt to Tech"
        },
        {
            "id": 863,
            "title": "Cambodia’s GFT Sector Suffered Setbacks"
        },
        {
            "id": 864,
            "title": "Government Reports Decrease in Human Trafficking"
        },
        {
            "id": 865,
            "title": "Call for Pepper Farmers to Apply to Export to China"
        },
        {
            "id": 866,
            "title": "Cambodian Exports to Japan Increase by 10.7%"
        },
        {
            "id": 867,
            "title": "PE Firm Tanncam Invests in Aussie Property Firm DCG"
        },
        {
            "id": 868,
            "title": "Richard Yim: How to Secure Quality Investment"
        },
        {
            "id": 869,
            "title": "Weather Warning Issued"
        },
        {
            "id": 870,
            "title": "Tax Revenue on the Rise"
        },
        {
            "id": 871,
            "title": "Five Inspiring Cambodian Entrepreneurs"
        },
        {
            "id": 872,
            "title": "EU Considers Reinstating EBA"
        },
        {
            "id": 873,
            "title": "Cambodia and the Netherlands Sign MoU to Boost Trade"
        },
        {
            "id": 874,
            "title": "PM Urges Collaboration Between ASEAN and EU"
        },
        {
            "id": 875,
            "title": "Cambodia Sees More than 515,000 Tourists in One Week"
        },
        {
            "id": 877,
            "title": "Phnom Penh Lecturer Awarded €67,000 for Mental Health Research"
        },
        {
            "id": 878,
            "title": "Cambodians Nod Towards China as Strong International Ally"
        },
        {
            "id": 879,
            "title": "Investment Guide Launched for Sihanoukville"
        },
        {
            "id": 880,
            "title": "Sihanoukville Airport Slated for Upgrade in January"
        },
        {
            "id": 881,
            "title": "Metfone and TVK Sign Cooperation Agreement"
        },
        {
            "id": 882,
            "title": "Making Digital Marketing Work"
        },
        {
            "id": 883,
            "title": "Five Inspiring Cambodian Founders"
        },
        {
            "id": 884,
            "title": "Global Issues Dampen Cambodia’s 2022 GDP Growth"
        },
        {
            "id": 885,
            "title": "Social Interventions Key to Curb Impact of Covid-19 and War in Ukraine"
        },
        {
            "id": 886,
            "title": "Twice-delayed PPAP’s Q3 Results Reveal Strong Earnings"
        },
        {
            "id": 887,
            "title": "Embracing Fintech in Cambodia"
        },
        {
            "id": 888,
            "title": "Rice Exports Rise by 10.67%"
        },
        {
            "id": 889,
            "title": "Pedestrian Zones Necessary for Urban Life"
        },
        {
            "id": 890,
            "title": "Second Round of Cambodia-UAE Trade Talks Start"
        },
        {
            "id": 891,
            "title": "Pig Farm Transforms Waste into Energy"
        },
        {
            "id": 892,
            "title": "Gasoline Price 4,100 riels Per Liter"
        },
        {
            "id": 893,
            "title": "Meet Memory Expert Eran Katz"
        },
        {
            "id": 894,
            "title": "PM Pledges Support for Waste-to-Energy Initiative"
        },
        {
            "id": 895,
            "title": "Cambodia’s Banking Sector Held Sway During Pandemic"
        },
        {
            "id": 896,
            "title": "Digital Marketing 101 for SMEs"
        },
        {
            "id": 897,
            "title": "World Bank Pours in $274m to Keep Cambodia’s Economy Buoyed Up"
        },
        {
            "id": 898,
            "title": "Rebuild Fiscal Buffers, Monitor High Credit Growth - AMRO"
        },
        {
            "id": 899,
            "title": "Call for Laws to Tackle Plastic Pollutants in Rivers"
        },
        {
            "id": 900,
            "title": "Social Protection Scheme Aims to Lift 60% Out of Poverty"
        },
        {
            "id": 901,
            "title": "Wat Ounalom’s Heritage Buildings Totally Razed"
        },
        {
            "id": 902,
            "title": "In Conversation with Memory Master Eran Katz"
        },
        {
            "id": 903,
            "title": "Davy Chou’s ‘Return to Seoul’ Makes Oscars’ Shortlist"
        },
        {
            "id": 904,
            "title": "High-Speed Train to Connect PP, Sihanoukville and the Thai Border"
        },
        {
            "id": 905,
            "title": "72.33% of Students Pass National Exams"
        },
        {
            "id": 906,
            "title": "Royal Railways Announces $24m Bond Issuance"
        },
        {
            "id": 907,
            "title": "ADB Funds $361.4m for Six Projects in Cambodia"
        },
        {
            "id": 908,
            "title": "Career Center Opens in Phnom Penh"
        },
        {
            "id": 909,
            "title": "$20m Pledged to Aid Marine and Coastal Fisheries"
        },
        {
            "id": 910,
            "title": "Law Enforcement Key to Save Mekong Dolphins from Extinction"
        },
        {
            "id": 911,
            "title": "Call for Sustainable Solutions to Combat Climate Change"
        },
        {
            "id": 912,
            "title": "Rice Farmers Turn to New Jobs Amid Tumbling Prices"
        },
        {
            "id": 913,
            "title": "Private Cloud Solutions Enter Cambodia"
        },
        {
            "id": 914,
            "title": "US Embassy Welcomes PM to Strengthen Bilateral Ties"
        },
        {
            "id": 915,
            "title": "Condo Oversupply Persists Amid Low FDI and Foreign Buyers"
        },
        {
            "id": 916,
            "title": "Spanish Guitarist to Perform in Phnom Penh"
        },
        {
            "id": 917,
            "title": "Eleventh Dolphin Found Dead in Mekong in 2022"
        },
        {
            "id": 918,
            "title": "Calls for Students to Master Tech Skills"
        },
        {
            "id": 919,
            "title": "Three New Cities Established"
        },
        {
            "id": 920,
            "title": "Miracle Elephant Calf Celebrates First Birthday"
        },
        {
            "id": 921,
            "title": "Collaboration Crucial for Regional Tourism Recovery"
        },
        {
            "id": 922,
            "title": "PPAP’s FY22 Net Profit to Rise 5%"
        },
        {
            "id": 923,
            "title": "2,534 High-Rise Buildings Completed by 2022"
        },
        {
            "id": 924,
            "title": "Cambodia Faces Drought in 2023"
        },
        {
            "id": 925,
            "title": "Introducing Cambodia’s Universities"
        },
        {
            "id": 926,
            "title": "Foreign Tourists to Reach 3m in 2023"
        },
        {
            "id": 927,
            "title": "ACLEDA Bank and Ministry of Civil Service Launch ID Card that Works as ATM Card"
        },
        {
            "id": 928,
            "title": "Metfone’s YouTube Channel Awarded Gold Play Button"
        },
        {
            "id": 929,
            "title": "AIA Cambodia Throws its Weight Behind SEA Games"
        },
        {
            "id": 930,
            "title": "Education Company Plans to List on CSX"
        },
        {
            "id": 931,
            "title": "Poipet Casino Blaze Kills at Least 19"
        },
        {
            "id": 932,
            "title": "Sihanoukville Port’s Earnings Fall 2.75%"
        },
        {
            "id": 933,
            "title": "Official Accused of Monkey Smuggling in the US on Bail"
        },
        {
            "id": 934,
            "title": "Prahok Season Starts in Cambodia"
        },
        {
            "id": 935,
            "title": "Famed Spanish Guitarist Joins RUFA Students on Stage"
        },
        {
            "id": 936,
            "title": "PM Urges Residents to Receive Covid-19 Booster"
        },
        {
            "id": 937,
            "title": "Cambodia-China Trade Reaches $14.5b"
        },
        {
            "id": 938,
            "title": "Poipet Fire Kills 26 and Injures 57"
        },
        {
            "id": 939,
            "title": "Project Aims to Promote Healthy Nutrition and Livelihoods"
        },
        {
            "id": 940,
            "title": "2022 Under Review"
        },
        {
            "id": 941,
            "title": "$114m Bridge to be Built Over Mekong River in Kratie"
        },
        {
            "id": 942,
            "title": "PM Calls for Conservation Areas to Protect Dolphins"
        },
        {
            "id": 943,
            "title": "‘The Last Breath of the Tonle Sap’ at Angkor Photo Festival"
        },
        {
            "id": 944,
            "title": "12 Protected Mekong Turtles Found Dead During Raid"
        },
        {
            "id": 945,
            "title": "Total of 88 Gambling Licenses Issued in 2022"
        },
        {
            "id": 946,
            "title": "From Finance to Pioneering Cambodia’s Animation Sector"
        },
        {
            "id": 947,
            "title": "Cashew Exports Fall by 34.65%"
        },
        {
            "id": 948,
            "title": "2023: A Gloomy Outlook of Continued Recovery Amid Global Strife"
        },
        {
            "id": 949,
            "title": "Plans to Boost Agricultural Exports and Increase Rice Prices in 2023"
        },
        {
            "id": 950,
            "title": "International Jewelry Manufacturer to Open Cambodian Factory in 2024"
        },
        {
            "id": 951,
            "title": "Tributes Paid to “Fearless” Journalist Nate Thayer"
        },
        {
            "id": 952,
            "title": "ACLEDA Bank Reports Double Digit Growth In 2022"
        },
        {
            "id": 953,
            "title": "DNA Tests Start on Six Unidentified Bodies from Poipet Casino Blaze"
        },
        {
            "id": 954,
            "title": "Angkor Wat Ticket Sales Soar by 2,000%"
        },
        {
            "id": 955,
            "title": "Kiripost and BBC Media Action Roll Out Journalism Training Program"
        },
        {
            "id": 956,
            "title": "Talking Business with Entrepreneurship Guru Stephen Paterson"
        },
        {
            "id": 957,
            "title": "ACLEDA Bank Opens 264th Branch Seven Days a Week"
        },
        {
            "id": 958,
            "title": "Metfone Crowned Best Company to Work for in Asia"
        },
        {
            "id": 959,
            "title": "Restoration of Ta Prohm’s South Gate Starts"
        },
        {
            "id": 960,
            "title": "Rice Exports Total 637,004 Tons in 2022"
        },
        {
            "id": 961,
            "title": "Cambodia Ready to Welcome Chinese Tourists"
        },
        {
            "id": 962,
            "title": "Call to Pull Plug on Re-Release of \"Provocative\" Song"
        },
        {
            "id": 964,
            "title": "Walmart in Talks to Expand Business in Cambodia"
        },
        {
            "id": 965,
            "title": "Investing in Clearing Minefields Helps Communities"
        },
        {
            "id": 966,
            "title": "Collapsed Dam Causes Water Scarcity in Sihanoukville"
        },
        {
            "id": 967,
            "title": "Kao Kim Hourn Assumes Role as ASEAN Secretary-General"
        },
        {
            "id": 968,
            "title": "No Further Coupon Rate Hikes for One-year Bond Tenors"
        },
        {
            "id": 969,
            "title": "Chinese Arrivals Remain Constant Despite Loosening of Restrictions"
        },
        {
            "id": 970,
            "title": "CDRI Marks Three Decades of Research to Help Develop the Nation"
        },
        {
            "id": 971,
            "title": "ABA Signs Exclusive Sponsorship Deal for SEA and Para Games"
        },
        {
            "id": 972,
            "title": "Five Year Suspension on Prepaid Income Tax for Textile Sector"
        },
        {
            "id": 973,
            "title": "Licadho Ordered to Remove Rap Song from Online Platforms"
        },
        {
            "id": 974,
            "title": "Cambodia and Turkey Aim to Hit $1b in Bilateral Trade"
        },
        {
            "id": 975,
            "title": "Water Restored After Sihanoukville Dam Collapse"
        },
        {
            "id": 976,
            "title": "Half Million Tourists Travel Cambodia in One Week"
        },
        {
            "id": 977,
            "title": "New Siem Reap Airport Slated to Open in October"
        },
        {
            "id": 978,
            "title": "CSX Sets Ambitious Targets for 2023 as GDP Picks Up"
        },
        {
            "id": 979,
            "title": "PPAP Handled 20% More Container TEUs in 2022"
        },
        {
            "id": 980,
            "title": "Ministry of Social Affairs Official Quizzed Over $387,000 Theft"
        },
        {
            "id": 981,
            "title": "PM Sends Appreciation for 70 Year Friendship with Japan"
        },
        {
            "id": 982,
            "title": "Critically-Endangered White-Shouldered Ibis Population on Rise"
        },
        {
            "id": 983,
            "title": "Cambodia’s Economy Slated to Grow 6% in 2023"
        },
        {
            "id": 984,
            "title": "Born to Engineer"
        },
        {
            "id": 985,
            "title": "PPAP’s FY’22 Revenue Lifted Despite Q4 Dip"
        },
        {
            "id": 986,
            "title": "$106m Collected in Unpaid Vehicle Tax"
        },
        {
            "id": 987,
            "title": "PM Heads to Maldives to Strengthen Bilateral Ties"
        },
        {
            "id": 988,
            "title": "Flights Into Cambodia to Increase to 280,900 in 2023"
        },
        {
            "id": 989,
            "title": "Draft Law on Land Policy for Sihanoukville Approved"
        },
        {
            "id": 990,
            "title": "Sar Kheng Reaffirms Commitment to Stamping out Money Laundering"
        },
        {
            "id": 991,
            "title": "MOU Signing Between UYFC and EZECOM on \"Digital Collaboration\""
        },
        {
            "id": 992,
            "title": "Chinese Tourists Slow to Arrive, and Not in the Way We Know It"
        },
        {
            "id": 993,
            "title": "Cambodia Trains Ukrainian Deminers to Clear UXOs"
        },
        {
            "id": 994,
            "title": "From Phnom Penh to Silicon Valley"
        },
        {
            "id": 995,
            "title": "Talks to Set Legal Age to Buy Alcohol at 18"
        },
        {
            "id": 996,
            "title": "Cashew Policy Gateway to Export Market"
        },
        {
            "id": 997,
            "title": "PM’s Personal Call for China to Build High-Speed Railway"
        },
        {
            "id": 998,
            "title": "Over-indebted Cambodian Farmers Rely on Microfinance Amid Climate Change"
        },
        {
            "id": 999,
            "title": "Exhibit Urges Rainforest and Wildlife Conservation"
        },
        {
            "id": 1000,
            "title": "Dry Season Floods Plague Kandal and Phnom Penh"
        },
        {
            "id": 1001,
            "title": "Overcoming Adversity to Become a Digital Entrepreneur"
        },
        {
            "id": 1002,
            "title": "A Blueprint for Sustainable Tourism in SE Asia"
        },
        {
            "id": 1003,
            "title": "Forum to Introduce Arbitration Services"
        },
        {
            "id": 1004,
            "title": "Bilateral Relations Between Maldives and Cambodia Tighten"
        },
        {
            "id": 1005,
            "title": "MoH Dishes Out CNY Health Warnings"
        },
        {
            "id": 1006,
            "title": "Royal Group Signs Agreement to Build Koh Rong Airport"
        },
        {
            "id": 1007,
            "title": "CGCC Gave $92m Business Loans in 2022"
        },
        {
            "id": 1008,
            "title": "CSX Secures First Green Bond"
        },
        {
            "id": 1009,
            "title": "Cambodia’s “Bright Future” in E-Commerce"
        },
        {
            "id": 1010,
            "title": "BFIs Code of Conduct Fully Implemented"
        },
        {
            "id": 1011,
            "title": "866 Unemployed Hotel Workers Set to Receive Cash Allowance"
        },
        {
            "id": 1012,
            "title": "Authorities Earn $29m from Foreign Worker Fees"
        },
        {
            "id": 1013,
            "title": "Food Prices Rise Ahead of Chinese New Year"
        },
        {
            "id": 1014,
            "title": "NCAC Resolves 31 Disputes Worth $90m"
        },
        {
            "id": 1015,
            "title": "Lunar New Year Celebrations Start in the Capital"
        },
        {
            "id": 1016,
            "title": "Boosting Business for Cambodia’s Cashew Farmers"
        },
        {
            "id": 1017,
            "title": "Legal Recognition of LGBT Families Essential for Social Integration"
        },
        {
            "id": 1018,
            "title": "French Trade Minister’s Visit to Strengthen Bilateral Relations"
        },
        {
            "id": 1019,
            "title": "Businesses Remain Closed After Lunar New Year Celebrations"
        },
        {
            "id": 1020,
            "title": "Free Vocational Training for 1.5m Students in 2024"
        },
        {
            "id": 1021,
            "title": "SEA Games Racks Up $100m Bill"
        },
        {
            "id": 1022,
            "title": "PP-Poipet High-speed Train Will Cost $4b"
        },
        {
            "id": 1023,
            "title": "Warning Issued Over Lethal Contaminated Cough Syrup"
        },
        {
            "id": 1024,
            "title": "Automotive and Electronics Sectors to Receive $2b Cash Boost"
        },
        {
            "id": 1025,
            "title": "Battambang Airport in Line for Upgrade to Receive Tourists"
        },
        {
            "id": 1026,
            "title": "Construction Sector Faces “Credit Crunch”"
        },
        {
            "id": 1027,
            "title": "Cambodia Pins Hopes on Removal from Money Laundering Watchlist"
        },
        {
            "id": 1028,
            "title": "High-Speed Railway to Connect PP and HCMC"
        },
        {
            "id": 1029,
            "title": "PM Slams School for Barbering Boys’ Hair"
        },
        {
            "id": 1030,
            "title": "$200m Gov’t Bond to Set Benchmark"
        },
        {
            "id": 1031,
            "title": "Incentives Rolled Out as Solution to Sihanoukville’s Abandoned Buildings"
        },
        {
            "id": 1032,
            "title": "Kun Khmer Confirmed at SEA Games Amid Thai Rage"
        },
        {
            "id": 1033,
            "title": "WHO to Help ID Toxic Levels in Confiscated Cough Syrups"
        },
        {
            "id": 1034,
            "title": "Slowing Inflation Fails to Ease Cost-of-Living Burden"
        },
        {
            "id": 1035,
            "title": "Amru Rice Unveils $5m Expansion Plan"
        },
        {
            "id": 1036,
            "title": "Authorities Mull Water Connection Between PP and Kampot"
        },
        {
            "id": 1037,
            "title": "Call for UK to Invest in Cambodia’s Agriculture Sector"
        },
        {
            "id": 1038,
            "title": "Ngeth Chou: Investment, Business and Life"
        },
        {
            "id": 1039,
            "title": "Building Sustainable Cities"
        },
        {
            "id": 1040,
            "title": "Digitizing Cambodia’s Health Sector"
        },
        {
            "id": 1041,
            "title": "CSOs’ Funding Suffered in 2021 Due to Laws"
        },
        {
            "id": 1042,
            "title": "Cambodia Defends Efforts to Stamp Out Human Trafficking"
        },
        {
            "id": 1043,
            "title": "1,709 Killed on Cambodia’s Roads in 2022"
        },
        {
            "id": 1044,
            "title": "Thousands of Garment Workers’ Jobs at Risk"
        },
        {
            "id": 1045,
            "title": "Siem Reap Ranks Fourth Top Trending Travel Destination 2023"
        },
        {
            "id": 1046,
            "title": "Cambodia Sees Slight Improvements on Corruption Index"
        },
        {
            "id": 1047,
            "title": "MoC Earns $15m in 2022"
        },
        {
            "id": 1048,
            "title": "Architect Turned Hotelier Sets Sights on Sustainable Designs"
        },
        {
            "id": 1049,
            "title": "$3.4b Collected in Taxes in 2022"
        },
        {
            "id": 1050,
            "title": "Smart Axiata Recruits New CEO"
        },
        {
            "id": 1051,
            "title": "Telcotech Signs Deal with Kampus to Expand Data Center Footprint"
        },
        {
            "id": 1052,
            "title": "Calls to Extend Maternity Leave to Six Months"
        },
        {
            "id": 1053,
            "title": "National Domain Name Rolled Out"
        },
        {
            "id": 1054,
            "title": "Tributes Paid to Long-serving Journalist"
        },
        {
            "id": 1055,
            "title": "Call for 7,000 Volunteers to Help at SEA Games"
        },
        {
            "id": 1056,
            "title": "Imprisoned Union Leader Scoops Human Rights Defender Award"
        },
        {
            "id": 1057,
            "title": "Fuel Prices Rise Again Amid Global Crisis"
        },
        {
            "id": 1058,
            "title": "Illegal Online Loan Advertisers Threatened with Legal Action"
        },
        {
            "id": 1059,
            "title": "Strong “Wheeled” - Cambodians Learn Skills to ‘Resurrect’ Broken Wheelchairs"
        },
        {
            "id": 1060,
            "title": "Evaluation of Cambodia’s Media Landscape Gets Underway"
        },
        {
            "id": 1061,
            "title": "Businesses Warned to Pay Taxes"
        },
        {
            "id": 1062,
            "title": "MoC Plans to Launch Five Business Centers in China"
        },
        {
            "id": 1063,
            "title": "German President to Visit Cambodia to Bolster Bilateral Ties"
        },
        {
            "id": 1064,
            "title": "Nout Daro: Drawing his Own Life Path"
        },
        {
            "id": 1065,
            "title": "Cambodia Hopes to Export 1,000 Tonnes of Rice to the Philippines"
        },
        {
            "id": 1066,
            "title": "Ajinomoto Signs Deal to Become Official Sponsor of SEA Games"
        },
        {
            "id": 1067,
            "title": "High-Skilled Labour Key to Develop Economy"
        },
        {
            "id": 1068,
            "title": "Recruitment Drive for Teachers and Officials After Two-Year Freeze"
        },
        {
            "id": 1069,
            "title": "Cellcard and Ezecom Launch First Customer Digital Experience Centers"
        },
        {
            "id": 1070,
            "title": "Koh Rong Sanloem Businesses Given Until Feb 9 to Leave"
        },
        {
            "id": 1071,
            "title": "IFAD Visits Cambodia to Stimulate Inclusive Agricultural Growth"
        },
        {
            "id": 1072,
            "title": "Cambodia Welcomes First Chinese Tourists"
        },
        {
            "id": 1073,
            "title": "Cambodian Academics Debate Chatbot Pros and Cons"
        },
        {
            "id": 1074,
            "title": "Training to Stamp Out Illegal Trafficking of Cultural Heritage Launches"
        },
        {
            "id": 1075,
            "title": "Pledge to Stamp Out Informal Money Lenders"
        },
        {
            "id": 1076,
            "title": "ADB and Cambodia Post Bank Sign $10m Loan for MSMEs"
        },
        {
            "id": 1077,
            "title": "Bilateral Political Consultations Start Between France and Cambodia"
        },
        {
            "id": 1078,
            "title": "Film Buffs Prepare for European Film Festival Cambodia"
        },
        {
            "id": 1079,
            "title": "Premier League Team Signs Cambodian-American Footballer"
        },
        {
            "id": 1080,
            "title": "SERC, CSX Review MJQE’s Mainboard IPO Application"
        },
        {
            "id": 1081,
            "title": "Almost Half A Million Undocumented Cambodian Workers Worldwide"
        },
        {
            "id": 1082,
            "title": "Ochheuteal Beach Fence Torn Down Amid Public Outcry"
        },
        {
            "id": 1083,
            "title": "Cambodia Earns $92m in Rice Exports in January"
        },
        {
            "id": 1084,
            "title": "City Slums Aware of Cleanliness but Aggrieved by Poor Sanitation and Floods"
        },
        {
            "id": 1085,
            "title": "Social Security Week to Tackle Efficiency and Transparency"
        },
        {
            "id": 1086,
            "title": "Concern Over Cambodia’s Climbing Debt"
        },
        {
            "id": 1087,
            "title": "PM Secures Road, Rail and River Investment During China Trip"
        },
        {
            "id": 1088,
            "title": "Hun Sen and Chinese President Meet in Beijing"
        },
        {
            "id": 1089,
            "title": "Evicted Island Business Owners Call for Compensation"
        },
        {
            "id": 1090,
            "title": "PPAP’s Container Throughput Falls 26% in January"
        },
        {
            "id": 1091,
            "title": "Acleda Posts Highest-Ever Net Profit at $182m in FY’22"
        },
        {
            "id": 1092,
            "title": "NagaCorp Bets on Becoming “Sizable Riverine Integrated Resort” in Asia Pacific"
        },
        {
            "id": 1093,
            "title": "PPSP Q4 Net Profit Nosedives, No Land Sale"
        },
        {
            "id": 1094,
            "title": "Raft of Topics Discussed During PM’s China Visit"
        },
        {
            "id": 1095,
            "title": "VoD Shuttered After PM Rejects Apology over News Report"
        },
        {
            "id": 1096,
            "title": "Cambodia’s National E-Sports Team Announced for SEA Games"
        },
        {
            "id": 1097,
            "title": "Grave Concerns Raised over VOD Closure"
        },
        {
            "id": 1098,
            "title": "Scheme to Reduce Child Internet Exploitation Launches"
        },
        {
            "id": 1099,
            "title": "PPAP’s Revenue Falls 15% as Port Ops Decline in January"
        },
        {
            "id": 1100,
            "title": "Pestech Posts Net Loss, Lower Revenue in Q2’23"
        },
        {
            "id": 1101,
            "title": "Ibis Budget Brand Opens in Phnom Penh"
        },
        {
            "id": 1102,
            "title": "IFAD Pledges $194m to Aid 100,000 Farmers"
        },
        {
            "id": 1103,
            "title": "PM Offers VOD Staff Jobs at State Organizations"
        },
        {
            "id": 1104,
            "title": "PM Talks Tourism with Laotian Premier During Visit"
        },
        {
            "id": 1105,
            "title": "Water Sales and Lower Taxes Raises PPWSA’s Q4 Profits"
        },
        {
            "id": 1106,
            "title": "Cambodia’s First Crowdfunding Platform Sets $1m Target for Team Cambodia"
        },
        {
            "id": 1107,
            "title": "Social Protection Scheme Bolsters Nation’s Healthcare"
        },
        {
            "id": 1108,
            "title": "Fighting Crime in Sihanoukville Has Been Tough, Says Governor"
        },
        {
            "id": 1109,
            "title": "PM Requests Cambodia Becomes a member of the Chinese CIPS"
        },
        {
            "id": 1110,
            "title": "Smart Logistics Complex to Position Cambodia as Leading Regional Logistics Hub"
        },
        {
            "id": 1111,
            "title": "German President Concludes Cambodia Visit"
        },
        {
            "id": 1112,
            "title": "Karmalink Hits the Big Screen as Cambodia’s First Sci-fi Film"
        },
        {
            "id": 1113,
            "title": "Metfone Celebrates 14th Anniversary"
        },
        {
            "id": 1114,
            "title": "Evicted Island Businesses’ Deadline Extended"
        },
        {
            "id": 1115,
            "title": "Prasac’s Q4 Net Profit up 18% at $47m"
        },
        {
            "id": 1116,
            "title": "Cambodia’s Cashew Players’ Plans to Strengthen the Sector for Export"
        },
        {
            "id": 1117,
            "title": "US Named Cambodia's Largest Partner For Exports and China For Imports"
        },
        {
            "id": 1118,
            "title": "Kulen Water Becomes Exclusive Water Sponsor for SEA Games"
        },
        {
            "id": 1119,
            "title": "Vattanac Brewery Becomes Premium Sponsor for SEA Games"
        },
        {
            "id": 1120,
            "title": "Precious Angkorian Relics Returned to the Kingdom"
        },
        {
            "id": 1121,
            "title": "Media 101 Club Helping Cambodians Navigate Media and Online Landscapes"
        },
        {
            "id": 1122,
            "title": "Bond Issuer Royal Railway’s 4Q’22 Net Loss Balloons to $1.8m"
        },
        {
            "id": 1123,
            "title": "Edtech Startup Secures $275,000 Investment"
        },
        {
            "id": 1124,
            "title": "Axiata Group Strengthens Commitment to Cambodia"
        },
        {
            "id": 1125,
            "title": "Push to Promote Ecotourism"
        },
        {
            "id": 1126,
            "title": "South Korea to Increase Cambodian Workers to 10,000"
        },
        {
            "id": 1127,
            "title": "Athletes Ready Themselves for SEA Games"
        },
        {
            "id": 1128,
            "title": "AFD Celebrates 30 Years Investing in Cambodia's Development"
        },
        {
            "id": 1129,
            "title": "Kofi and SNV Sign MoU to Elevate Kingdom’s Coffee to Export Standards"
        },
        {
            "id": 1130,
            "title": "CSX Index Eight-month High as Stocks Rally on Acleda’s Earnings, New IPOs"
        },
        {
            "id": 1131,
            "title": "MoU Signed to Stamp Out Counterfeit Goods"
        },
        {
            "id": 1132,
            "title": "Project Launched to Include At-Risk Farmers in Social Security Scheme"
        },
        {
            "id": 1133,
            "title": "How to Snag a Fulbright Scholarship"
        },
        {
            "id": 1134,
            "title": "Exhibit Offers New Perspectives"
        },
        {
            "id": 1135,
            "title": "Bird Flu Kills Girl in Prey Veng"
        },
        {
            "id": 1136,
            "title": "Metfone Receives Lauded Medal from the Government"
        },
        {
            "id": 1137,
            "title": "Father of Girl Who Died of Bird Flu Tests Positive"
        },
        {
            "id": 1138,
            "title": "Rearing Cambodia’s Buffalo Milk Market"
        },
        {
            "id": 1139,
            "title": "Microfinance to Tap into WASH Sector"
        },
        {
            "id": 1140,
            "title": "‘Dare to Fail and Explore’, says Fulbright Alumnus"
        },
        {
            "id": 1141,
            "title": "PPAP’s FY’22 $15m Net Profit Surpasses Target"
        },
        {
            "id": 1142,
            "title": "Push to Develop Climate-Resilient Agriculture"
        },
        {
            "id": 1143,
            "title": "Cambodian E-gamers Gear Up to Battle for the Kingdom"
        },
        {
            "id": 1144,
            "title": "Cambodia Removed from FATF Grey List"
        },
        {
            "id": 1145,
            "title": "Project Aims to Strengthen Safe Finance in Communities"
        },
        {
            "id": 1146,
            "title": "Father of Girl Who Died of Bird Flu Tests Negative"
        },
        {
            "id": 1147,
            "title": "Cambodia Misses Target of Exporting 1m Tons of Rice"
        },
        {
            "id": 1148,
            "title": "Forum Tackles Sexual Harassment at Work"
        },
        {
            "id": 1149,
            "title": "Cambodia Gears up to Host Mekong Tourism Forum"
        },
        {
            "id": 1150,
            "title": "Boosting Cambodia's Global Reputation and Business Opportunities"
        },
        {
            "id": 1151,
            "title": "Vocational Training A Key Component to Cambodia’s Development"
        },
        {
            "id": 1152,
            "title": "Management Area Implemented to Protect Mekong Dolphins"
        },
        {
            "id": 1153,
            "title": "Evicted Island Businesses Start to Relocate"
        },
        {
            "id": 1154,
            "title": "Art As a Tool to Promote Mental Well-Being"
        },
        {
            "id": 1155,
            "title": "Visit Cambodia Year 2023 Campaign Aims to Draw 4m Tourists"
        },
        {
            "id": 1156,
            "title": "Increasing Safety for Female Journalists"
        },
        {
            "id": 1157,
            "title": "Fuel Decrease of 100 Riel Provides Small Reprieve for Population"
        },
        {
            "id": 1158,
            "title": "ICT Company Embraces Emerging HospitaliTech"
        },
        {
            "id": 1159,
            "title": "From Living on a Landfill to Filmmaker"
        },
        {
            "id": 1160,
            "title": "Study Compares Living Standards in Boreys and Non-Boreys"
        },
        {
            "id": 1161,
            "title": "Sihanoukville Port Sees Red in Q4’22"
        },
        {
            "id": 1163,
            "title": "Startup Tenbox Raises First Seed Investment"
        },
        {
            "id": 1164,
            "title": "ACLEDA KHQR Available at All 7-Eleven Stores in Cambodia"
        },
        {
            "id": 1165,
            "title": "The Capital Through the Eyes of A Lens"
        },
        {
            "id": 1166,
            "title": "Refinancing Risk prompts Moody's to Review NagaCorp's B2 Ratings for Downgrade"
        },
        {
            "id": 1167,
            "title": "Kids Encouraged to Read Ahead of National Reading Day"
        },
        {
            "id": 1168,
            "title": "Center to Increase Women Journalists’ Safety and Access to Legal Aid to Launch"
        },
        {
            "id": 1169,
            "title": "Suspended Factory Workers to Receive Allowances, Says PM"
        },
        {
            "id": 1170,
            "title": "Cambodia Promotes Tourism at World’s Leading Travel Trade Show"
        },
        {
            "id": 1171,
            "title": "Photographers Invited to Join Collective"
        },
        {
            "id": 1172,
            "title": "AI-powered Spellchecker for Khmer to Raise Language Skills"
        },
        {
            "id": 1173,
            "title": "MJQE Closer to IPO Launch as CSX Grants Approval in Principle"
        },
        {
            "id": 1174,
            "title": "Encouraging Women to Step Out of Traditional Gender Roles"
        },
        {
            "id": 1175,
            "title": "Systemic Failure Contributed to Women’s Murder, Licadho Reports"
        },
        {
            "id": 1176,
            "title": "Strategic Plan Launched to Address Cooling"
        },
        {
            "id": 1177,
            "title": "Ezecom Celebrating 15th Anniversary of Shaping and Innovating Technology Sector Beyond Kingdom"
        },
        {
            "id": 1178,
            "title": "BookMeBus Founder & CEO Navigating his Startup Through the Pandemic"
        },
        {
            "id": 1179,
            "title": "Kampong Chhnang Port to Push Exports"
        },
        {
            "id": 1180,
            "title": "Amru Receives EMIA Investment to Expand into Global Markets"
        },
        {
            "id": 1181,
            "title": "The Potential Power of Solar in Cambodia"
        },
        {
            "id": 1182,
            "title": "First Start-Up & Innovation Festival Takes to Stage"
        },
        {
            "id": 1183,
            "title": "The Cost and Benefits of BRI projects, Investments in Cambodia"
        },
        {
            "id": 1184,
            "title": "TikTok Signs Deal to be Premium Sponsor for SEA Games"
        },
        {
            "id": 1185,
            "title": "Public Campaign Unveiled to Stop Littering Nationwide"
        },
        {
            "id": 1186,
            "title": "Cellcard Crowned Cambodia’s Fastest Mobile Network"
        },
        {
            "id": 1187,
            "title": "Shout-out for Sponsors to Shape Cambodia’s Next Generation of Film-makers"
        },
        {
            "id": 1188,
            "title": "Smart Axiata Marks 14 Years of Service"
        },
        {
            "id": 1189,
            "title": "Anchor Beer Becomes Eighth Premium Sponsor for SEA Games"
        },
        {
            "id": 1190,
            "title": "PM’s Push for Cambodia to Become Major Cashew Exporter"
        },
        {
            "id": 1191,
            "title": "Cellcard Scoops Six OpenSignal Awards"
        },
        {
            "id": 1192,
            "title": "GTI FY’22 Net Profit Triples, Revenue Dips"
        },
        {
            "id": 1193,
            "title": "A $42.8m Project to Help Vulnerable Adapt to Climate Change Given Green Light"
        },
        {
            "id": 1194,
            "title": "$4m Pumped into Improving Nutrition in Schools"
        },
        {
            "id": 1195,
            "title": "PWSA FY’22 Net Profit Sees 16% Contraction"
        },
        {
            "id": 1196,
            "title": "Cellcard Named 9th SEA Games Premium Sponsor"
        },
        {
            "id": 1197,
            "title": "Sihanoukville Selected to Transform into Smart City"
        },
        {
            "id": 1198,
            "title": "Digitalisation Drive Gives MSMEs a Business Boost"
        },
        {
            "id": 1199,
            "title": "Cambodia Airways Named 10th SEA Games’ Premium Sponsor"
        },
        {
            "id": 1200,
            "title": "PM Calls for Calm After Collapse of Two US Banks"
        },
        {
            "id": 1201,
            "title": "Cellcard Clinches Opensignal Global Rising Star Award"
        },
        {
            "id": 1202,
            "title": "Cambodia to Sell 1 GW of Renewable Energy to Singapore"
        },
        {
            "id": 1203,
            "title": "ACLEDA to Introduce Cross-Border Payments in Laos and Vietnam"
        },
        {
            "id": 1204,
            "title": "ACLEDA Best Partner for Safe Assets, Says Senior Official"
        },
        {
            "id": 1205,
            "title": "Tackling Access to Water in Cambodia"
        },
        {
            "id": 1206,
            "title": "Buses Need to Be More Accessible for People with Disabilities"
        },
        {
            "id": 1207,
            "title": "Cambodia and UAE Negotiate Trade Deal"
        },
        {
            "id": 1208,
            "title": "Priceless Khmer Treasures Return Home"
        },
        {
            "id": 1209,
            "title": "Prioritize Passion When Choosing University Major"
        },
        {
            "id": 1210,
            "title": "Workshop Reinforces Ban on Forced Labour"
        },
        {
            "id": 1211,
            "title": "Cambodia's First Sweeping Machine"
        },
        {
            "id": 1212,
            "title": "Cambodian Authorities Urged to Probe Forced Labor in Factories"
        },
        {
            "id": 1213,
            "title": "Cambodian Perspective: Silicon Valley Bank's Collapse & Lessons Learned"
        },
        {
            "id": 1214,
            "title": "Sustainable Building Materials Crafted from Water Hyacinths"
        },
        {
            "id": 1215,
            "title": "King Lights Official SEA Games Torch"
        },
        {
            "id": 1216,
            "title": "Call for $1 Donations to Support Elephant Conservation"
        },
        {
            "id": 1217,
            "title": "Cellcard Scoops Prestigious “Best Digital Lifestyle Provider 2023” Award"
        },
        {
            "id": 1218,
            "title": "Cambodia to Host Asia Pride Games 2023"
        },
        {
            "id": 1219,
            "title": "Cambodia Launches Khmer Digital Literacy Programme"
        },
        {
            "id": 1220,
            "title": "M’Pai Bay: Open for Business"
        },
        {
            "id": 1221,
            "title": "Tath Nika: An Advocate for Equality for People with Disabilities"
        },
        {
            "id": 1222,
            "title": "Warning Issued Over Digital Security"
        },
        {
            "id": 1223,
            "title": "Schools Off During SEA and ASEAN Para Games"
        },
        {
            "id": 1224,
            "title": "Real Estate Giants Sign Deal to Develop Koh Pich"
        },
        {
            "id": 1225,
            "title": "Cambodia and Vietnam Sign Trade Deals"
        },
        {
            "id": 1226,
            "title": "ACLEDA Honored as Third Biggest Corporate Taxpayer of 2022"
        },
        {
            "id": 1227,
            "title": "Motivation, Self-Belief and Determination Key to Success, Says Start-up Founder"
        },
        {
            "id": 1228,
            "title": "China Pledges to Speed Up Phnom Penh-Poipet Expressway Project"
        },
        {
            "id": 1229,
            "title": "Water Shortages Reported in Phnom Penh and Takhmao"
        },
        {
            "id": 1230,
            "title": "ACLEDA Mobile Users Can Use QR Payments in Vietnam"
        },
        {
            "id": 1231,
            "title": "National Science, Technology and Innovation Day Launched"
        },
        {
            "id": 1232,
            "title": "Earth Hour Highlights the Importance of the Environment"
        },
        {
            "id": 1233,
            "title": "Niche in Auto, Green Energy Sectors Can Lure EU Business"
        },
        {
            "id": 1234,
            "title": "Malaysia and Cambodia to Sign Recruitment MoUs"
        },
        {
            "id": 1235,
            "title": "Get Your Child Closer to Their Dreams with Shrewsbury International School Phnom Penh's Scholarship Programme"
        },
        {
            "id": 1236,
            "title": "Lighthouse Club Cambodia Holds Fundraiser"
        },
        {
            "id": 1237,
            "title": "End to “Dodgy Investments” as Cambodia Exits FATF’s Grey List"
        },
        {
            "id": 1238,
            "title": "Cambodia and Malaysia to Raise Imports, Bust Crime and Develop Halal Industry"
        },
        {
            "id": 1239,
            "title": "HEINEKEN Brightens Prek Eng’s Future with Solar Streetlight Donation"
        },
        {
            "id": 1240,
            "title": "Social Health Insurance Scheme Extended to Tuk-Tuk Drivers"
        },
        {
            "id": 1241,
            "title": "Smart Axiata Receives Gold Award for Tax Compliance"
        },
        {
            "id": 1242,
            "title": "Call for Stakeholders to Facilitate PP-SR Expressway Study"
        },
        {
            "id": 1243,
            "title": "SEA Games Opening and Closing Ceremony Tickets on Sale"
        },
        {
            "id": 1244,
            "title": "Water Shortages Plague Phnom Penh Residents"
        },
        {
            "id": 1245,
            "title": "First Destination Siem Reap Day Aims to Boost Tourism"
        },
        {
            "id": 1246,
            "title": "Cellcard to Go Public Soon"
        },
        {
            "id": 1247,
            "title": "Pandemic Hits Artists’ Livelihoods"
        },
        {
            "id": 1248,
            "title": "AFD Pledges $435m for Cambodian Development Projects"
        },
        {
            "id": 1249,
            "title": "Preserving Traditional Khmer Arts"
        },
        {
            "id": 1250,
            "title": "Upcycling Fashion"
        },
        {
            "id": 1251,
            "title": "Free Access to Watch SEA Games"
        },
        {
            "id": 1252,
            "title": "Author Advocates for More Reading"
        },
        {
            "id": 1253,
            "title": "TikTok’s New Rules Strengthen User Safety"
        },
        {
            "id": 1254,
            "title": "Porsche to Exit Cambodia"
        },
        {
            "id": 1255,
            "title": "Urgent Call Not to Waste Water Amid Shortages"
        },
        {
            "id": 1256,
            "title": "Ox Cart Races Return to Kampong Speu"
        },
        {
            "id": 1257,
            "title": "USAID Launches Campaign to Encourage Early Childhood Development"
        },
        {
            "id": 1258,
            "title": "YEAC Signs MoU to Strengthen Cambodia’s SMEs"
        },
        {
            "id": 1259,
            "title": "Empowering Women to Handcraft Eco-Friendly Products"
        },
        {
            "id": 1260,
            "title": "First Science, Technology, and Innovation Day a Resounding Success"
        },
        {
            "id": 1261,
            "title": "Urgent Need to Safeguard Mekong River, Experts Say"
        },
        {
            "id": 1262,
            "title": "Foodpanda Cambodia Restructures Post-Pandemic"
        },
        {
            "id": 1263,
            "title": "Ratanakiri Governor Seeks Airport Investment"
        },
        {
            "id": 1264,
            "title": "Economy to Grow 5.5% in 2023 and 6% by 2024"
        },
        {
            "id": 1265,
            "title": "Read to Reduce Stress, Suggests Philanthropist"
        },
        {
            "id": 1266,
            "title": "Digital Menu Scanning Startup Published on Android OS"
        },
        {
            "id": 1267,
            "title": "Ezecom Hosts Life-Saving Blood Donation Drive"
        },
        {
            "id": 1268,
            "title": "Cellcard Announces Launch of Initial Public Offering"
        },
        {
            "id": 1269,
            "title": "Rise in Booze Consumption Prompts Fresh Calls for Alcohol Advert Ban"
        },
        {
            "id": 1270,
            "title": "Securing a Scholarship to Study Abroad During the Pandemic"
        },
        {
            "id": 1271,
            "title": "Power Plan Focuses on Renewable Energy"
        },
        {
            "id": 1272,
            "title": "Mengly J. Quach Education Gets In-Principle Green Light for IPO"
        },
        {
            "id": 1273,
            "title": "US Fed Rate Hikes Pinch Cambodian Pockets"
        },
        {
            "id": 1274,
            "title": "PM Appointed Honorary President of Cambodia Oknha Association"
        },
        {
            "id": 1275,
            "title": "Vientiane Declaration Pledges to Protect the Mekong River"
        },
        {
            "id": 1276,
            "title": "Calls to Tighten Smoking Laws"
        },
        {
            "id": 1277,
            "title": "Mining Company Produces 6 Tons of Gold in Mondulkiri"
        },
        {
            "id": 1278,
            "title": "Private Investors Sought for $55m Ecotourism Project"
        },
        {
            "id": 1279,
            "title": "Retrofitting Existing Residential Neighborhoods into Superblocks of Livable Neighborhoods"
        },
        {
            "id": 1280,
            "title": "Cambodia Approves Five Power Development Projects"
        },
        {
            "id": 1281,
            "title": "Network of 500km of Hiking Trails Planned for the Kingdom"
        },
        {
            "id": 1282,
            "title": "Cambodians Urged to Take Health Measures Against Heat"
        },
        {
            "id": 1283,
            "title": "Eight Cambodian Workers Killed in Thai Road Smash"
        },
        {
            "id": 1284,
            "title": "Tiffy Army FC Terminates Long Meng Hav’s Contract After Violence on the Pitch"
        },
        {
            "id": 1285,
            "title": "Football’s Olympic Torch Stops in Cambodia"
        },
        {
            "id": 1286,
            "title": "Cambodia’s Tourism Roadmap"
        },
        {
            "id": 1287,
            "title": "19 Japanese Deported Accused of Illegal Online Scams"
        },
        {
            "id": 1288,
            "title": "Exports Fall 5.7% to $5.4 billion"
        },
        {
            "id": 1289,
            "title": "Cambodia Smashes World Record for Most Paper Hearts"
        },
        {
            "id": 1290,
            "title": "Border Trade Agreement with Vietnam Presents Huge Benefits"
        },
        {
            "id": 1291,
            "title": "Siem Reap Hotels 90% Full for KNY"
        },
        {
            "id": 1292,
            "title": "Photography Exhibition Showcases Diverse Stories of Capital Dwellers"
        },
        {
            "id": 1293,
            "title": "Podcast Promotes Self-Awareness and Power of Thought"
        },
        {
            "id": 1294,
            "title": "Innovative Rainfall Gauge Wins Regional Competition"
        },
        {
            "id": 1295,
            "title": "Providing Shelter and Kindness to Cambodia's Most Vulnerable"
        },
        {
            "id": 1296,
            "title": "Skateistan Launches Online Skateboard Fundraising Drive"
        },
        {
            "id": 1297,
            "title": "Strategy Aims to Strengthen Garment Sector"
        },
        {
            "id": 1298,
            "title": "MoU Signed For India-Cambodia Cross-Border Payments"
        },
        {
            "id": 1299,
            "title": "Guidelines Issued to Stabilize Construction and Retail Sector"
        },
        {
            "id": 1300,
            "title": "Phnom Penh Port Q1 Revenue Down 13%"
        },
        {
            "id": 1301,
            "title": "Three Tour Operators Close"
        },
        {
            "id": 1302,
            "title": "National Assembly Approves Cambodia-Vietnam Border Trade Agreement"
        },
        {
            "id": 1303,
            "title": "IFC to Help Cambodia Become Southeast Asian Logistics Hub"
        },
        {
            "id": 1304,
            "title": "Two Companies to Invest $40 Million in Cambodian Islands"
        },
        {
            "id": 1305,
            "title": "Mengly J. Quach Education Kicks-off Roadshows for a $10 million IPO"
        },
        {
            "id": 1306,
            "title": "New Tax Law Passed"
        },
        {
            "id": 1307,
            "title": "ADB Urges Green Investment Ramp Up"
        },
        {
            "id": 1308,
            "title": "Coca-Cola Seals Deal to be SEA Games Official Sparkling Drinks Sponsor"
        },
        {
            "id": 1309,
            "title": "Cashew Nut Exports Tumble Almost 13% in Q1"
        },
        {
            "id": 1310,
            "title": "NBC Closes 104 Rural Credit Institutions"
        },
        {
            "id": 1311,
            "title": "Ezecom Named SEA Games’ Official Internet Provider"
        },
        {
            "id": 1312,
            "title": "Pride Cambodia Organization Officially Launches"
        },
        {
            "id": 1313,
            "title": "From Child Farmer to Published Author"
        },
        {
            "id": 1314,
            "title": "OCIC and BIG C Ink Deal to Open Hypermarket in Chroy Changvar"
        },
        {
            "id": 1315,
            "title": "From Martial Arts Fan to Hollywood"
        },
        {
            "id": 1316,
            "title": "Improving Cambodia’s Agriculture Sector"
        },
        {
            "id": 1317,
            "title": "Thousands Gather in Phnom Penh to Watch Esports Battle"
        },
        {
            "id": 1318,
            "title": "New Container Terminal to be Constructed at Sihanoukville Autonomous Port"
        },
        {
            "id": 1319,
            "title": "Thousands Queue for SEA Games’ Football Tickets"
        },
        {
            "id": 1320,
            "title": "Accused Fraudsters Arrested for Conning $40m from 2,461 Families"
        },
        {
            "id": 1321,
            "title": "SEA Games Aims to Elevate Cambodia’s International Image"
        },
        {
            "id": 1322,
            "title": "River Bank Collapse Impacts 40 Kandal Houses"
        },
        {
            "id": 1323,
            "title": "Fashion Show Throws Spotlight on River Pollution"
        },
        {
            "id": 1324,
            "title": "Pride Festival Provides Inclusive Platform for LGBTQI+ Community"
        },
        {
            "id": 1325,
            "title": "Cellcard Crowned Best Digital Services Innovator"
        },
        {
            "id": 1326,
            "title": "$20.91m in VAT Collected in Three Months"
        },
        {
            "id": 1327,
            "title": "Measures Needed to Cope with Future Tourism Influx"
        },
        {
            "id": 1328,
            "title": "Cellcard’s Innovative Launches Enable Customer Digital Lifestyle"
        },
        {
            "id": 1329,
            "title": "MEF, ABA Bank Partner to Develop Digital Economy and Fintech"
        },
        {
            "id": 1330,
            "title": "Historian and Custodian of Cambodia Heritage Darryl Collins Dies"
        },
        {
            "id": 1331,
            "title": "Cambodia’s First YIGF Will Empower Digital Champs"
        },
        {
            "id": 1332,
            "title": "PM Repeals Sub-decree to Protect Mekong Dolphins"
        },
        {
            "id": 1333,
            "title": "PM Calls for Order from SEA Games’ Spectators"
        },
        {
            "id": 1334,
            "title": "Tycoon Chea Saron and Eight Staff Sent to Pretrial Detention Accused of Fraud"
        },
        {
            "id": 1335,
            "title": "Cambodia Successfully Hosts Mekong Tourism Forum"
        },
        {
            "id": 1336,
            "title": "Cambodia National Football Team Confident of Win"
        },
        {
            "id": 1337,
            "title": "ACLEDA to Pay Record Highest Dividend in May"
        },
        {
            "id": 1338,
            "title": "Cambodia Scores 4-0 Win Against Timor Leste in SEA Games’ Football"
        },
        {
            "id": 1339,
            "title": "Handicraft Businesses Face Challenging Times"
        },
        {
            "id": 1340,
            "title": "MoU Provides MSMEs with Easier Access to Finance"
        },
        {
            "id": 1341,
            "title": "CSX Sets Target of $100m in Daily Stock Prices by 2030"
        },
        {
            "id": 1342,
            "title": "Fisheries Sector Receives Innovative Equipment to Increase Market Access"
        },
        {
            "id": 1343,
            "title": "Cambodia Wins Two Points in Men's Chess Event"
        },
        {
            "id": 1344,
            "title": "Laos President and Former President of Timor-Leste to Attend SEA Games’ Opening Ceremony"
        },
        {
            "id": 1345,
            "title": "Sihanoukville in Line to Become Leading International Port Hub"
        },
        {
            "id": 1346,
            "title": "Cellcard Launches First E-Health Service Initiative"
        },
        {
            "id": 1347,
            "title": "Cambodia and the Philippines Draw 1-1 in Football"
        },
        {
            "id": 1348,
            "title": "Media Call to End Impunity Against Journalists"
        },
        {
            "id": 1349,
            "title": "Government Urged to Promote Freedom of the Press"
        },
        {
            "id": 1350,
            "title": "Indigenous Soup Helping Raise Profile of Ethnic Population"
        },
        {
            "id": 1351,
            "title": "$3m Project Aims to Elevate Mondulkiri Farmers’ Livelihoods"
        },
        {
            "id": 1352,
            "title": "Cambodia Defeats Singapore 3-0 in Men's Volleyball at SEA Games"
        },
        {
            "id": 1353,
            "title": "Cambodia’s Khan Jessa Defeats Singapore and Vietnam in Ne-Waza at SEA Games"
        },
        {
            "id": 1354,
            "title": "Cambodian Women's Football Team Secure 2-0 Victory Against Laos"
        },
        {
            "id": 1355,
            "title": "Cambodia Misses Out on Gold Medal for Ne-Waz, Earning A Silver For the Host Nation"
        },
        {
            "id": 1356,
            "title": "Cambodia’s Male Jiu-Jitsu Athletes Score First Gold Medal for Host Nation"
        },
        {
            "id": 1357,
            "title": "Cambodian Billiards’ Champ Secured Success in Korea"
        },
        {
            "id": 1358,
            "title": "Cambodia Delivers SEA Games’ Opening Ceremony Spectacular"
        },
        {
            "id": 1359,
            "title": "Cambodia Wins 4 Gold Medals in Bokator at 32nd SEA Games"
        },
        {
            "id": 1360,
            "title": "Cambodian “King of Chess” Wins Gold Medal in 5-Minute Rapid Chess"
        },
        {
            "id": 1361,
            "title": "Cambodian Women’s U-22 Make History Securing a Spot in the Semi-Finals"
        },
        {
            "id": 1362,
            "title": "Cambodian Men’s Basketball Team Win Gold in 3x3 Tournament"
        },
        {
            "id": 1363,
            "title": "Cambodia’s Women Basketball Team Loses out to Philippines in Semi-Finals"
        },
        {
            "id": 1364,
            "title": "Khan Jessa Clinches Gold Medal"
        },
        {
            "id": 1365,
            "title": "Higher NPL, Loan Provisioning Forecast this Year"
        },
        {
            "id": 1366,
            "title": "Cambodian Swimmer Misses Out on Medal at 50m Backstroke"
        },
        {
            "id": 1367,
            "title": "Cambodian Men's Football Team Lose 2-0 to Myanmar"
        },
        {
            "id": 1368,
            "title": "Cambodia Men's Doubles Petanque Make Finals"
        },
        {
            "id": 1369,
            "title": "Protection from Digital Security Threats"
        },
        {
            "id": 1370,
            "title": "Royal Oxen Predict Strong Harvest During Ploughing Ceremony"
        },
        {
            "id": 1371,
            "title": "Indonesia Clinches Gold in Men's Volleyball"
        },
        {
            "id": 1372,
            "title": "Pursuit of Education Pays Off"
        },
        {
            "id": 1373,
            "title": "Head of FFC Reverses Decision to Resign"
        },
        {
            "id": 1374,
            "title": "Sruong Pheavy Wins Gold Medal in Three Cushion Billiards"
        },
        {
            "id": 1375,
            "title": "Cambodia Women’s Doubles Petanque Lose Gold"
        },
        {
            "id": 1376,
            "title": "ACLEDA Records Strong Net Profit in Q1’23"
        },
        {
            "id": 1377,
            "title": "Frontier Myanmar Founder: Making Media Sustainable"
        },
        {
            "id": 1378,
            "title": "Winners Crowned for Sustainable Innovations in Heineken Sustainathon"
        },
        {
            "id": 1379,
            "title": "Pioneering $100,000 Project to Promote LGBT+ in Schools"
        },
        {
            "id": 1380,
            "title": "Pal Chhor Raksmy Wins Record Six Medals in Vovinam"
        },
        {
            "id": 1381,
            "title": "Cambodia Loses Out on Gold to Thailand in Men’s Doubles Petanque"
        },
        {
            "id": 1382,
            "title": "Central and Eastern Europe Represented by EuroCham in New Chapter"
        },
        {
            "id": 1383,
            "title": "PPSP Back in Black in Q1’23 with $5.7m Net Profit"
        },
        {
            "id": 1384,
            "title": "Thousands Fill Wat Botum Park to Watch Cambodia Take on Indonesia"
        },
        {
            "id": 1385,
            "title": "UNESCO-Cambodia Launch Report on Science, Tech and Innovation"
        },
        {
            "id": 1386,
            "title": "Waste Summit Throws Spotlight on Importance of Waste Separation"
        },
        {
            "id": 1387,
            "title": "100,000 Dogs to be Vaccinated Against Rabies in Phnom Penh"
        },
        {
            "id": 1388,
            "title": "Kun Khmer Athletes Clinch Eight Medals for Cambodia"
        },
        {
            "id": 1389,
            "title": "Cambodia's Hopes of Semi-Finals Dashed After Loss to Indonesia"
        },
        {
            "id": 1390,
            "title": "$60m World Bank Aid to Help Cambodia’s Solid Waste and Plastic Management"
        },
        {
            "id": 1391,
            "title": "Phnom Penh Internet Forum to Promote Digital Rights and Freedom"
        },
        {
            "id": 1392,
            "title": "Sar Kheng Tests Positive for Covid-19"
        },
        {
            "id": 1393,
            "title": "Keisuke Honda to Retire as Cambodian National Football Coach"
        },
        {
            "id": 1394,
            "title": "Going for Gold in Sports and Song"
        },
        {
            "id": 1395,
            "title": "Unions Hold Protest Against Adidas to Demand Compensation"
        },
        {
            "id": 1396,
            "title": "Indonesia Defeats Cambodia in Men’s Water Polo"
        },
        {
            "id": 1397,
            "title": "Cambodian Khmer Kun Fighters Bag 14 Medals"
        },
        {
            "id": 1398,
            "title": "Cambodia Wushu Team Wins Seven Medals"
        },
        {
            "id": 1399,
            "title": "Ten-men Indonesia Beats Vietnam to Reach SEA Games Football Final"
        },
        {
            "id": 1400,
            "title": "Educate Children in Financial Literacy via Stock Investment"
        },
        {
            "id": 1401,
            "title": "Cambodia’s Q1’23 Apparel Exports to Europe, North America Significantly Down"
        },
        {
            "id": 1402,
            "title": "Fourth and Final Gold Medal for Cambodian Taekwondo Star Sorn Seavmey"
        },
        {
            "id": 1403,
            "title": "Cambodian Swimmers Bag Two Golds and a Host of Medals in Finswimming"
        },
        {
            "id": 1404,
            "title": "Cambodia Taekwondo Athletes Show Potential at SEA Games"
        },
        {
            "id": 1405,
            "title": "After A Dismal Q1’23, Revenue Contraction Persists for Phnom Penh Port"
        },
        {
            "id": 1406,
            "title": "Cambodia Earns Gold in Traditional Boat Racing"
        },
        {
            "id": 1407,
            "title": "Long-term Expat Steve Porte Found"
        },
        {
            "id": 1408,
            "title": "Cambodian Women’s Football Team Lose Out On Bronze Against Thailand"
        },
        {
            "id": 1409,
            "title": "Turning Toddy Palm Cake to Bread"
        },
        {
            "id": 1410,
            "title": "Generative AI: A Threat to Copyright?"
        },
        {
            "id": 1411,
            "title": "Indonesia Clinch Gold in Men’s Football After Fraught Match"
        },
        {
            "id": 1412,
            "title": "Textile Industry Seeks Solutions for Circular Economy"
        },
        {
            "id": 1413,
            "title": "Hollywood Star Matt Dillon Named Patron of CIFF"
        },
        {
            "id": 1414,
            "title": "Rain Fails to Dash SEA Games’ Closing Ceremony Spectacular"
        },
        {
            "id": 1415,
            "title": "PPWSA Posts Higher Net Profit in Q1’23"
        },
        {
            "id": 1416,
            "title": "Cambodia Snag Silver in Men’s 5x5 Basketball"
        },
        {
            "id": 1417,
            "title": "Royal Railway Back in the Black in Q1’23"
        },
        {
            "id": 1418,
            "title": "Exhibition Highlights Art of Drag Queens"
        },
        {
            "id": 1419,
            "title": "World Bank Says Cambodia’s Economic Recovery is Strong"
        },
        {
            "id": 1420,
            "title": "App Aims to Encourage Cambodians to Donate to Charity"
        },
        {
            "id": 1421,
            "title": "Concerns Raised Over Shrinking Online Freedom"
        },
        {
            "id": 1422,
            "title": "In-depth Study into $1.7b Shipping Canal Given Green Light"
        },
        {
            "id": 1423,
            "title": "Preparations Underway for Cambodia to Host 12th ASEAN Para Games"
        },
        {
            "id": 1424,
            "title": "Liger Students Use Innovation to Highlight Threats of Climate Change"
        },
        {
            "id": 1425,
            "title": "Artist’s Ambition to Break Graffiti Stereotypes"
        },
        {
            "id": 1426,
            "title": "Efforts Needed for Cambodia to Fully Embrace Digitalization"
        },
        {
            "id": 1427,
            "title": "$300m Sihanoukville Tyre Factory Set to Tap into Cambodia’s Rubber Production"
        },
        {
            "id": 1428,
            "title": "Institut Pasteur Marks 70 Years in Cambodia"
        },
        {
            "id": 1429,
            "title": "World Famous Monk San Sochea Retires from Monkhood"
        },
        {
            "id": 1430,
            "title": "Is Phnom Penh’s Liquid Waste Management Good Enough?"
        },
        {
            "id": 1431,
            "title": "Thailand Punishes Players Involved in SEA Games’ Football Brawl"
        },
        {
            "id": 1432,
            "title": "Klahan9 Roadshow Academy Empowers Youth"
        },
        {
            "id": 1433,
            "title": "$82M Multi-Specialty Center at Calmette Hospital Inaugurated"
        },
        {
            "id": 1434,
            "title": "ODC Provides Data Literacy Training for Journalists"
        },
        {
            "id": 1435,
            "title": "Pestech Stays in Red in Q3’23, No Dividend Payout for FY’22"
        },
        {
            "id": 1436,
            "title": "Business Model Competition Showcases Cambodian Students’ Innovation"
        },
        {
            "id": 1437,
            "title": "River Tern Population Rebounds in Cambodia"
        },
        {
            "id": 1438,
            "title": "Khmer Angkor Training Art Club Calls for Support"
        },
        {
            "id": 1439,
            "title": "Call For Transparency in Extractive Industry Revenues"
        },
        {
            "id": 1440,
            "title": "“Walk A Mile In My Shoes As A Volunteer For Cambodia’s 32nd SEA Games With Me”"
        },
        {
            "id": 1441,
            "title": "Union Leader Chhim Sithar Jailed for Two Years"
        },
        {
            "id": 1442,
            "title": "Toyota Plant to Open in PPSEZ in July"
        },
        {
            "id": 1443,
            "title": "After the Boom, Cambodia’s Real Estate Sector Sees Red"
        },
        {
            "id": 1444,
            "title": "EV Assembly Plant Starts Operations in Kandal"
        },
        {
            "id": 1445,
            "title": "Cambodian E-sports Makes History With ASEAN Para Games Debut"
        },
        {
            "id": 1446,
            "title": "NGOs Launch Forum on Engagement in Public Financial Management"
        },
        {
            "id": 1447,
            "title": "International Youth Day is Celebrated in Phnom Penh"
        },
        {
            "id": 1448,
            "title": "Roomchang Dental Hospital Workshop Raises Emergency Response in Dentistry"
        },
        {
            "id": 1449,
            "title": "Real Estate and Construction Sector Needs Reform to Thrive"
        },
        {
            "id": 1450,
            "title": "Producing Coconut Oil to Address Migration"
        },
        {
            "id": 1451,
            "title": "German Embassy Talks MFI with Stakeholders"
        },
        {
            "id": 1452,
            "title": "New Smart Airport Aims to Drive More Tourists into Siem Reap"
        },
        {
            "id": 1453,
            "title": "Women with Disabilities Gain Funds to Expand Home-Based Businesses"
        },
        {
            "id": 1454,
            "title": "PWSA to Pay 10-year High Dividend for FY’22"
        },
        {
            "id": 1455,
            "title": "CP Cambodia Becomes Official Sponsor of ASEAN Para Games"
        },
        {
            "id": 1456,
            "title": "PM Pledges Spectacular ASEAN Para Games’ Opening and Closing Ceremonies"
        },
        {
            "id": 1457,
            "title": "Thalias and Almond Hospitality Groups Merge"
        },
        {
            "id": 1458,
            "title": "Net Gains from Asset Sale Double PAS’ Q1 Net Profit"
        },
        {
            "id": 1459,
            "title": "Cambodia’s First 3DA Billboards Land in the Capital"
        },
        {
            "id": 1460,
            "title": "China Gives Go-ahead to Import Fishery Products from Cambodia"
        },
        {
            "id": 1461,
            "title": "Kantha Bopha Hospital Calls for $2.50 Donations"
        },
        {
            "id": 1462,
            "title": "From Farm Boy to SEA Games’ Gold Medalist"
        },
        {
            "id": 1463,
            "title": "Bolstering Cambodia’s Oyster Farming Sector"
        },
        {
            "id": 1464,
            "title": "Soltilo Angkor FC Dissolved After Six Years of Football"
        },
        {
            "id": 1465,
            "title": "Innovation Festival Attracts Hundreds Tech Enthusiasts"
        },
        {
            "id": 1466,
            "title": "Preserving the Ancient Khmer Martial Art of Bokator"
        },
        {
            "id": 1467,
            "title": "Cambodia Hosts Impressive 12th ASEAN Para Games’ Opening Ceremony"
        },
        {
            "id": 1468,
            "title": "TikTok’s SEA Games’ Campaign Smashes Records"
        },
        {
            "id": 1469,
            "title": "Urbanland Unveils Borey Chankiri 2 Development"
        },
        {
            "id": 1470,
            "title": "Climate Risks on Cambodian Children"
        },
        {
            "id": 1471,
            "title": "Free Online Courses to Strengthen Tourism SMEs’ Digital and Financial Skills"
        },
        {
            "id": 1472,
            "title": "Koh Kong Families Settle in Long-running Land Dispute"
        },
        {
            "id": 1473,
            "title": "Cambodia Scores Bronze in ASEAN Para Games' Esports Event"
        },
        {
            "id": 1474,
            "title": "Idea Library Calls for Book Donations"
        },
        {
            "id": 1475,
            "title": "Project Aims to Awaken Young Farmers"
        },
        {
            "id": 1476,
            "title": "Apple Unveils $3,500 Mixed Reality Headset, Vision Pro"
        },
        {
            "id": 1477,
            "title": "Falling Orders Drag GTI into the Red in Q1"
        },
        {
            "id": 1479,
            "title": "Asian Stocks Mixed after Wall St Retreats on Concern Economy Weakening"
        },
        {
            "id": 1480,
            "title": "Hundreds of Journalists Strike to Demand Leadership Change at Biggest US Newspaper Chain"
        },
        {
            "id": 1481,
            "title": "Cambodia’s Esporters Prepare for Phnom Penh-Hosted Asia Cup"
        },
        {
            "id": 1482,
            "title": "SIM Card Bank Scam Warning Issued"
        },
        {
            "id": 1483,
            "title": "Asian Stocks Mixed as Wall St Inches toward Bull Market"
        },
        {
            "id": 1484,
            "title": "Wheat Prices Jump Following Collapse of Major Dam in Southern Ukraine"
        },
        {
            "id": 1485,
            "title": "Cambodia’s Sethisak Khuon to Sing in Madame Butterfly Opera"
        },
        {
            "id": 1486,
            "title": "$230m Mekong River Bridge to Connect with PP-Bavet Expressway"
        },
        {
            "id": 1487,
            "title": "Suspended Garment Workers to Receive Second Allowance Payout"
        },
        {
            "id": 1488,
            "title": "Artist Sou Sophy Lobbies for Conservation in Latest Exhibition"
        },
        {
            "id": 1489,
            "title": "Rekindling Ancient Cambodian Rice Art"
        },
        {
            "id": 1490,
            "title": "Gold Medal Para Athlete Aims to Inspire"
        },
        {
            "id": 1491,
            "title": "Asian Shares Slip Following Technology Selloff on Wall Street"
        },
        {
            "id": 1492,
            "title": "Vith Chantha Celebrates Third Gold Para Games’ Medal"
        },
        {
            "id": 1493,
            "title": "ACLEDA and CBC Ink Deal to Provide Credit Checks Via Mobile App"
        },
        {
            "id": 1494,
            "title": "Level Up Green Bonds to Close Gaps in Sustainable Infra Financing"
        },
        {
            "id": 1495,
            "title": "Cambodia and UAE to Sign Second Commerce Deal"
        },
        {
            "id": 1496,
            "title": "Cambodia Praised for Hosting Successful ASEAN Para Games"
        },
        {
            "id": 1497,
            "title": "Urgent Call for Global AI Governance"
        },
        {
            "id": 1498,
            "title": "Business Community Celebrates Champions of Glass Bottle Return Program"
        },
        {
            "id": 1499,
            "title": "ASEAN Para Games’ Closing Ceremony Pays Tribute to Competing Athletes"
        },
        {
            "id": 1500,
            "title": "Rooftop Solar Regulations Loosened"
        },
        {
            "id": 1501,
            "title": "China and HK Cambodia’s Top Rice Exporters in First Five Months of 2023"
        },
        {
            "id": 1502,
            "title": "ThaiQR Accessible at 1.5m Cambodian Retailers"
        },
        {
            "id": 1503,
            "title": "Nomadic Culture Event Takes Over Peak Mall"
        },
        {
            "id": 1504,
            "title": "Cambodia’s Garment Exports to Australia Increase"
        },
        {
            "id": 1505,
            "title": "Heatwave Hits Seaweed Growers"
        },
        {
            "id": 1506,
            "title": "Cambodian Photographer Receives World Recognition"
        },
        {
            "id": 1507,
            "title": "Asian Shares Mixed as Investors Await Fed Policy Decision, Price Data"
        },
        {
            "id": 1508,
            "title": "China Struggles with Weak post-COVID Economic Recovery"
        },
        {
            "id": 1509,
            "title": "Tapping Into AI’s Potential"
        },
        {
            "id": 1510,
            "title": "“Formidable” Journalist Nate Thayer’s Ashes Scattered in the Mekong"
        },
        {
            "id": 1511,
            "title": "Digital Skill Development Roadmap to Address Cambodia’s Skills Shortage"
        },
        {
            "id": 1512,
            "title": "NagaCorp’s Corporate Family Rating Downgraded, Outlook Negative"
        },
        {
            "id": 1513,
            "title": "First Premium Seaplane Service to Take Off in the Kingdom"
        },
        {
            "id": 1514,
            "title": "Australian Mining Company Produces 6,727kg of Gold in Three Years"
        },
        {
            "id": 1515,
            "title": "Nurturing A Green Economy"
        },
        {
            "id": 1516,
            "title": "UNICEF Donates $7m of Oxygen Therapy Medical Equipment"
        },
        {
            "id": 1517,
            "title": "Climate Financing Essential to Develop Sustainable Businesses"
        },
        {
            "id": 1518,
            "title": "AirAsia Resumes Flights Between Sihanoukville and KL and Bangkok"
        },
        {
            "id": 1519,
            "title": "BTS Turns 10. Seoul Lights up Landmarks to Celebrate"
        },
        {
            "id": 1520,
            "title": "Asia Markets Higher ahead of US Inflation, Fed Rates Decision"
        },
        {
            "id": 1521,
            "title": "PPAP’s Revenue Slips Again in May"
        },
        {
            "id": 1522,
            "title": "Japanese Farm to Grow Chilli Peppers Ripe for Export"
        },
        {
            "id": 1523,
            "title": "VannDa’s Tokyo Debut Excites Cambodian Fans in Japan"
        },
        {
            "id": 1524,
            "title": "GDT Denies Joy School’s Demand That Parents Pay Income Tax"
        },
        {
            "id": 1525,
            "title": "Regulators Take Aim at AI to Protect Consumers and Workers"
        },
        {
            "id": 1526,
            "title": "Asian Stocks Mixed after US Inflation Cools"
        },
        {
            "id": 1527,
            "title": "The Beatles are Releasing their 'last' Record. AI Helped Make it Possible"
        },
        {
            "id": 1528,
            "title": "MLC Special Fund 2023 Pumps $2m into Nine Cambodian Projects"
        },
        {
            "id": 1529,
            "title": "Navigating the Digital World"
        },
        {
            "id": 1530,
            "title": "Workers Given Three Paid Days Off to Vote"
        },
        {
            "id": 1531,
            "title": "PM Calls for Investigation into Confiscated Homes"
        },
        {
            "id": 1532,
            "title": "Travellers Demand Immersive Experiences, Says Phare Circus"
        },
        {
            "id": 1533,
            "title": "Long-awaited Vietnam Energy Plan Aims to Boost Renewables, but Fossil Fuels still in the Mix"
        },
        {
            "id": 1534,
            "title": "Asia Shares Rise as Fed Holds Rates steady while Hinting of Hikes ahead"
        },
        {
            "id": 1535,
            "title": "Seven Million Vehicles on Cambodia’s Roads"
        },
        {
            "id": 1536,
            "title": "Tycoon Chea Saron Fined More Than $4,000 and Has Licence Revoked"
        },
        {
            "id": 1537,
            "title": "TikTok Launches SEA Socio-Economic Impact Report 2023"
        },
        {
            "id": 1538,
            "title": "Deal Inked for $19m Biodiverse Landscapes Fund"
        },
        {
            "id": 1539,
            "title": "TikTok Planning to Fuel e-Commerce Business in Southeast Asia with Billions in Investments"
        },
        {
            "id": 1540,
            "title": "Meta Hosts Session on Creating Impactful Content"
        },
        {
            "id": 1541,
            "title": "Voters Can Now See Who's Behind Political Ads On Facebook"
        },
        {
            "id": 1542,
            "title": "Asian Shares Track Wall Street Rally, Bank of Japan Stands pat"
        },
        {
            "id": 1543,
            "title": "Banks Trained to Prioritise Client Protection"
        },
        {
            "id": 1544,
            "title": "TikTok to Invest $12.2m to Help 120,000 MSMEs Transition Online"
        },
        {
            "id": 1545,
            "title": "Cambodian Journalist Awarded by US for Human Trafficking Reporting"
        },
        {
            "id": 1546,
            "title": "‘Are We Not Humans?’, Domestic Workers Ask"
        },
        {
            "id": 1547,
            "title": "Overcoming Adversity to Champion Blind Football"
        },
        {
            "id": 1548,
            "title": "Asia Follows Wall St lower as US, Chinese Foreign Ministers Meet"
        },
        {
            "id": 1549,
            "title": "Wages are Finally Rising in Japan, as Inflation Eats away at Consumer Gains"
        },
        {
            "id": 1550,
            "title": "Australian Agribusiness Explores Potential in Cambodia"
        },
        {
            "id": 1551,
            "title": "Myth in Motion: A Thought-Provoking Exhibition"
        },
        {
            "id": 1552,
            "title": "MLVT Stresses Need for Technical and Professional Skills"
        },
        {
            "id": 1553,
            "title": "7-Eleven to Set Up 100 Stores in Cambodia by Year-End"
        },
        {
            "id": 1554,
            "title": "InsurTech Company Launches Digital Car Insurance Product"
        },
        {
            "id": 1555,
            "title": "$6.4m Footwear Factory Inaugurated in Kampong Speu"
        },
        {
            "id": 1556,
            "title": "EFPC Makes Recommendations to Stimulate Socio-Economic Growth"
        },
        {
            "id": 1557,
            "title": "$188m Road and Water Loans to be Signed with Japan"
        },
        {
            "id": 1558,
            "title": "Breastfeeding Promoted in Kampong Thom"
        },
        {
            "id": 1559,
            "title": "Blinken and Xi Pledge to Stabilize deteriorated US-China Ties, but China Rebuffs the main US Request"
        },
        {
            "id": 1560,
            "title": "UN Members Adopt first-ever Treaty to Protect Marine Life in the high Seas"
        },
        {
            "id": 1561,
            "title": "Official Launch of GLN Cross Border CPM QR Payments in Cambodia"
        },
        {
            "id": 1562,
            "title": "International Yoga Day Celebration"
        },
        {
            "id": 1563,
            "title": "Campaign Calls for Pharma Giant to Cut Cost of HIV Meds"
        },
        {
            "id": 1564,
            "title": "New ‘Kamnotra’ Database Shares Critical Data on Land, Royal Gazettes"
        },
        {
            "id": 1565,
            "title": "Bak Kheng Water Treatment Plant is Inaugurated"
        },
        {
            "id": 1566,
            "title": "Sovrin Magazine to Suspend its Print Fashion Edition"
        },
        {
            "id": 1567,
            "title": "Singapore Ride-hailing Firm Grab Slashes 1,000 jobs in biggest Layoff since Pandemic"
        },
        {
            "id": 1568,
            "title": "Foreign Companies are Shifting Investment out of China as Confidence Wanes, Business Group Says"
        },
        {
            "id": 1569,
            "title": "Parents Pursue Civil Suit Against Milk Powder Company"
        },
        {
            "id": 1570,
            "title": "Borey and Real Estate Businesses Found Operating Without License"
        },
        {
            "id": 1571,
            "title": "Exports to Thailand Increase 9.47% in First Five Months of 2023"
        },
        {
            "id": 1572,
            "title": "MoU Signed with Singapore to Provide Vocational Training for 1.5m Cambodians"
        },
        {
            "id": 1573,
            "title": "AirAsia Cambodia Maiden Flight Take-Off in Q4"
        },
        {
            "id": 1574,
            "title": "Chinese e-Commerce Giant Alibaba Announces new CEO and Chairman in major Management Reshuffle"
        },
        {
            "id": 1575,
            "title": "Meet Lean Chan Lamy, the Woman Behind Bay Slek Jek"
        },
        {
            "id": 1576,
            "title": "Online Business Registration Made Easier"
        },
        {
            "id": 1577,
            "title": "Tax Obligations Explained to Car Dealers"
        },
        {
            "id": 1578,
            "title": "Warning Issued Over SMS Phishing Scams"
        },
        {
            "id": 1579,
            "title": "Twitter Faces 'Stress Test' of Europe's Tough New Big Tech Rules"
        },
        {
            "id": 1580,
            "title": "Climate Activist Nakate Urges Rich Countries to Cancel Debt, Grant Climate Finance at Paris Summit"
        },
        {
            "id": 1581,
            "title": "Debt-plagued Zambia Reaches Deal with China, Other Nations to Rework $6.3B in Loans, French say"
        },
        {
            "id": 1582,
            "title": "Prahok Being Primed for Export"
        },
        {
            "id": 1583,
            "title": "Twenty-seven Startups and SMEs Receive $5,000 to $20,000 Grants"
        },
        {
            "id": 1584,
            "title": "Officials Reject Claim that Battambang Villa is Impacting Riverbanks"
        },
        {
            "id": 1585,
            "title": "Student Develops UAI App"
        },
        {
            "id": 1586,
            "title": "Smashing Gender Stereotypes"
        },
        {
            "id": 1587,
            "title": "The Rise of the Super App in Cambodia"
        },
        {
            "id": 1588,
            "title": "Chamkar 3 Kampot Pepper Brings Unique Spice to the Local Market"
        },
        {
            "id": 1589,
            "title": "Cambodia to Receive Over 20 Million Tourists This Year"
        },
        {
            "id": 1590,
            "title": "Malaysia Says It Will Take Legal Action against Meta over Harmful Content on Facebook"
        },
        {
            "id": 1591,
            "title": "Iconic Architect Lu Ban Hap Dies Aged 92"
        },
        {
            "id": 1592,
            "title": "China's Premier Says Economic Growth is Accelerating and the Country Can Hit its 5% Target This Year"
        },
        {
            "id": 1593,
            "title": "Ministry Warns Content Creators to Curb “Offensive” Online Material"
        },
        {
            "id": 1594,
            "title": "Amret, PPSP and Golden Tree to Issue $95m Green, Sustainability Bonds"
        },
        {
            "id": 1595,
            "title": "Battambang Villa Owner Dismantles Front Yard"
        },
        {
            "id": 1596,
            "title": "Three Arrested After Defrauding Bank Customer of $100,000"
        },
        {
            "id": 1597,
            "title": "Contracts Signed with Farming Families and Rice Production Groups"
        },
        {
            "id": 1598,
            "title": "Cellcard Lists Stock on CSX"
        },
        {
            "id": 1599,
            "title": "Cambodian Designer Speaks at Global Fashion Summit"
        },
        {
            "id": 1600,
            "title": "2,700 People Tricked into Working for Cybercrime Syndicates Rescued in Philippines"
        },
        {
            "id": 1601,
            "title": "Threatened by Shortages, Electric Car Makers Race for Supplies of Lithium for Batteries"
        },
        {
            "id": 1602,
            "title": "Nearly 36 million in Europe May Have Experienced Long COVID, World Health Organization Official Says"
        },
        {
            "id": 1603,
            "title": "Heineken Commemorates 150 Years of Good Times"
        },
        {
            "id": 1604,
            "title": "Deal Inked to Fast-Track Cambodian Work Permits for Thailand"
        },
        {
            "id": 1605,
            "title": "US Band Promotes People with Disabilities Through Music and Art"
        },
        {
            "id": 1606,
            "title": "The Rise of Messaging App Telegram in Cambodia"
        },
        {
            "id": 1607,
            "title": "Mengly J. Quach Education Officially Listed on CSX"
        },
        {
            "id": 1608,
            "title": "SEA and Para Game Medallists Awarded $6.6m"
        },
        {
            "id": 1609,
            "title": "S’Art Festival Shines Spotlight on Cambodian Urban Art"
        },
        {
            "id": 1610,
            "title": "Korean Air Unveils New Aircraft on PP to Seoul Route"
        },
        {
            "id": 1611,
            "title": "Authorities Reject Concerns Over Adoption Laws"
        },
        {
            "id": 1612,
            "title": "IPO Timing, Uncertain Economy, Slay Cellcard and MJQE Subscription"
        },
        {
            "id": 1613,
            "title": "SERC, CiC Prep Members on IPOs, Securities Market"
        },
        {
            "id": 1614,
            "title": "PM Trades Facebook for Telegram"
        },
        {
            "id": 1615,
            "title": "US Embassy Celebrates 247th Independence Day"
        },
        {
            "id": 1616,
            "title": "In Workaholic Japan, 'Job Leaving Agents' Help People Escape the Awkwardness of Quitting"
        },
        {
            "id": 1617,
            "title": "Survey Shows China's Manufacturing Contracted in June as Export Orders Decreased"
        },
        {
            "id": 1618,
            "title": "Ten Workers Die at Ratanakiri Banana Plantation"
        },
        {
            "id": 1619,
            "title": "Fighting for Equality"
        },
        {
            "id": 1620,
            "title": "Discover the “Pearl of Asia”, Phnom Penh"
        },
        {
            "id": 1621,
            "title": "Sri Lanka's Parliament Approves a Debt Restructuring Plan in an Attempt to Overcome Economic Crisis"
        },
        {
            "id": 1622,
            "title": "Six Die in Tuol Kork Fire"
        },
        {
            "id": 1623,
            "title": "Recycled Waste to Green Charcoal"
        },
        {
            "id": 1624,
            "title": "AIIB Lends $100m to ACLEDA for SME Loans"
        },
        {
            "id": 1625,
            "title": "112 Trucks Extinguish Blaze at Toul Kork KTV Fire That Killed Eight People"
        },
        {
            "id": 1626,
            "title": "IFC Ombudsman calls for Compliance Investigation on Six MFIs"
        },
        {
            "id": 1627,
            "title": "Pathmazing Connects CCF Children and Grandmothers with a Piece of History"
        },
        {
            "id": 1628,
            "title": "Business Travel for Indonesians to Australia Will be Made Easier in a Deal Between National Leaders"
        },
        {
            "id": 1629,
            "title": "Apple is Now the First Public Company to be Valued at $3 Trillion"
        },
        {
            "id": 1630,
            "title": "Underground Parking Lots to Open in Phnom Penh"
        },
        {
            "id": 1631,
            "title": "The Road to Empowerment"
        },
        {
            "id": 1632,
            "title": "Meta is Set to Take on Twitter with a Rival App Called Threads"
        },
        {
            "id": 1633,
            "title": "Stock Market Today: Asia Sinks After a Survey Shows China's Industrial Activity is Weakening"
        },
        {
            "id": 1634,
            "title": "Thailand-Cambodia Border Reopens"
        },
        {
            "id": 1635,
            "title": "NBC Launches Cambodian Shared Switch"
        },
        {
            "id": 1636,
            "title": "Australia Unveils Plans to Develop Three Agri-Food Industrial Parks"
        },
        {
            "id": 1637,
            "title": "Facebook Faces Legal Setback in EU Court Decision on Data Privacy and Ads"
        },
        {
            "id": 1638,
            "title": "Meta Takes Aim at Twitter with the Launch of Rival App Threads"
        },
        {
            "id": 1639,
            "title": "Monetary Tightening to Benefit Cambodian Capital Market in Time, say RAC"
        },
        {
            "id": 1640,
            "title": "Access to Finance, Rise of the Riel and Inflation, with CBC"
        },
        {
            "id": 1641,
            "title": "Economy to Grow 5.5% in 2023, Says NBC"
        },
        {
            "id": 1642,
            "title": "Tesla's Autopilot Driver-Assist System Gets Closer Look as US Seeks Details on Recent Changes"
        },
        {
            "id": 1643,
            "title": "What is Threads? All Your Questions About Meta's New Twitter Rival, Answered"
        },
        {
            "id": 1644,
            "title": "The Hidden Beauty in ASEAN: Bringing SEA Games and Urban Planning to Cambodia"
        },
        {
            "id": 1645,
            "title": "MSMEs Urged to Reduce Carbon Footprint"
        },
        {
            "id": 1646,
            "title": "‘How Can We Help Grow Your Economy?’ Australia asks Cambodia"
        },
        {
            "id": 1647,
            "title": "'Clone' or Competitor? Users and Lawyers Compare Twitter and Threads"
        },
        {
            "id": 1648,
            "title": "Cambodia’s First Starlink Deployed from Vanilla Farm"
        },
        {
            "id": 1649,
            "title": "CBC’s CEO Talks Digitalization, Alternative Data and Financial Health Checks"
        },
        {
            "id": 1650,
            "title": "Talks Held with Alibaba to Promote Cambodian Rice"
        },
        {
            "id": 1651,
            "title": "Pathmazing Donates $15,000 of SEA Games’ Merchandise to ISF"
        },
        {
            "id": 1652,
            "title": "Importance of Public-Private Partnerships in Health Sector"
        },
        {
            "id": 1653,
            "title": "Matt Dillon’s Love of Cambodia, ‘City of Ghosts’ and his Return"
        },
        {
            "id": 1654,
            "title": "Cambodian Threads Users Share Their Thoughts"
        },
        {
            "id": 1655,
            "title": "Cambodia Turns Challenges into Opportunities for Australian Investors"
        },
        {
            "id": 1656,
            "title": "Australia Deepens Economic Ties with ASEAN"
        },
        {
            "id": 1657,
            "title": "Cellcard FY’22 Net Profit Up 46%"
        },
        {
            "id": 1658,
            "title": "MJQE Net Profit Skyrockets to $2.3m in FY22"
        },
        {
            "id": 1659,
            "title": "Cross-Border QR Payments Between China and Cambodia Launch"
        },
        {
            "id": 1660,
            "title": "International Trade Down 13% in First Half of 2023"
        },
        {
            "id": 1661,
            "title": "Election Campaign Sparks Slump in Local Tourists, Says MoT"
        },
        {
            "id": 1662,
            "title": "Premium Seaplane Slated for Take-Off Late-2023 to Early-2024"
        },
        {
            "id": 1663,
            "title": "Cambodia and Myanmar Strongest Reliant on Chinese Trade in ASEAN"
        },
        {
            "id": 1664,
            "title": "Tuk Tuk Drivers Can Register for NSSF Cards"
        },
        {
            "id": 1665,
            "title": "Rosewood Phnom Penh Crowned Best Hotel in Asia"
        },
        {
            "id": 1666,
            "title": "Foreign Investments Up $45.8b in Q1’23 - NBC"
        },
        {
            "id": 1667,
            "title": "PM Launches App to Provide Timely News and Entertainment"
        },
        {
            "id": 1668,
            "title": "Fuel Stations Busted for Conning Customers"
        },
        {
            "id": 1669,
            "title": "Struggles of Life on the Boat"
        },
        {
            "id": 1670,
            "title": "Will AI Replace Journalists?"
        },
        {
            "id": 1671,
            "title": "Food Content Creator Boosts Cambodian Food and Tourism"
        },
        {
            "id": 1672,
            "title": "Dissecting the New Tax Law"
        },
        {
            "id": 1673,
            "title": "Cambodia Fintech Company Elevating Access to Finance"
        },
        {
            "id": 1674,
            "title": "PPAP’s Jan-June Revenue Down 19%"
        },
        {
            "id": 1675,
            "title": "Technovation Cambodia Nurtures Young Female Talent"
        },
        {
            "id": 1676,
            "title": "Digibox Becomes Cambodia’s First Apple Premium Reseller"
        },
        {
            "id": 1677,
            "title": "Chinese Yuan Not to be Legalized in Cambodia, NBC Confirms"
        },
        {
            "id": 1678,
            "title": "Streets Are Catalysts For Lively and Safe Urban Spaces"
        },
        {
            "id": 1679,
            "title": "Britain Officially Joins an Asia-Pacific Trade Group that Includes Japan and 10 Other Nations"
        },
        {
            "id": 1680,
            "title": "VSO Project Promotes Green Economies on Tonle Sap Lake"
        },
        {
            "id": 1681,
            "title": "New Rules of Origin Law Ends Long-Standing Ambiguity"
        },
        {
            "id": 1682,
            "title": "Providing Young Cambodians with Skills to Thrive"
        },
        {
            "id": 1683,
            "title": "New Investment Law Offers Attractive Incentives for Agriculture"
        },
        {
            "id": 1684,
            "title": "Aquaculturist Association Asks China for Support to Elevate the Sector"
        },
        {
            "id": 1685,
            "title": "MoC Unveils Law to Protect Real Estate Customers"
        },
        {
            "id": 1686,
            "title": "TAFTAC Calls for End to Unsustainable Wood Used to Power Industry"
        },
        {
            "id": 1687,
            "title": "Facebook Parent Meta Makes Public its ChatGPT Rival Llama"
        },
        {
            "id": 1688,
            "title": "Spotlight Shone on Cambodian’s Consumer Habits"
        },
        {
            "id": 1689,
            "title": "Capital Injection Puts ABA Bank’s Shareholders’ Capital at $1.7b"
        },
        {
            "id": 1690,
            "title": "Importance of a Distinctive Logo"
        },
        {
            "id": 1691,
            "title": "Seeing Art Through The Eyes Of An Apsara Artist"
        },
        {
            "id": 1692,
            "title": "Report Internet Connection Problems via MPTC Speed Test App - Chea Vandeth"
        },
        {
            "id": 1693,
            "title": "Explainer: NSSF - How Cambodian Workers Are Protected Under A Social Security Safety Net"
        },
        {
            "id": 1694,
            "title": "“Life is About Learning”- KAS Fellow Likhedy Tells Youths"
        },
        {
            "id": 1695,
            "title": "Musk Says Twitter to Change Logo to \"X\" from the Bird. Changes Could Come as Early as Monday"
        },
        {
            "id": 1696,
            "title": "In 'Barbie,' 'Oppenheimer' Smash Success, Audiences Send Message to Hollywood: Give Us Something New"
        },
        {
            "id": 1697,
            "title": "Educational Tourism Receives A Boost"
        },
        {
            "id": 1698,
            "title": "MPWT Sets Price of 1,600 Riel per kWh for Electric Vehicles"
        },
        {
            "id": 1699,
            "title": "Learning Lessons Working at Microsoft"
        },
        {
            "id": 1700,
            "title": "Art Exhibit Explores Individualism in Post-War Cambodia"
        },
        {
            "id": 1701,
            "title": "ADB Approves $40m Loan to Improve Public Services"
        },
        {
            "id": 1702,
            "title": "Hun Sen Resigns, Handing Over Premiership to His Son"
        },
        {
            "id": 1703,
            "title": "Nagacorp Regains Momentum - 1H’23 Net Profit Up $83m"
        },
        {
            "id": 1704,
            "title": "Hun Manet: Cambodia’s Next PM"
        },
        {
            "id": 1705,
            "title": "Hopes New PM Will Prioritize Development and Society"
        },
        {
            "id": 1706,
            "title": "As Twitter Fades to X, TikTok Steps up with New Text-based Posts"
        },
        {
            "id": 1707,
            "title": "Hun Manet’s Takeover Leaves Little Implications for Policy Continuity, Economic Growth"
        },
        {
            "id": 1708,
            "title": "Social Media Ad Reach in Cambodia Shifts in 2023: Facebook vs TikTok"
        },
        {
            "id": 1709,
            "title": "Siem Reap Angkor International Airport Set To Open in October"
        },
        {
            "id": 1710,
            "title": "Samsung Unveils Foldable Smartphones in a Bet on Devices with Bending Screens"
        },
        {
            "id": 1711,
            "title": "As E-bikes Proliferate, So Do Deadly Fires Blamed on Exploding Lithium-ion Batteries"
        },
        {
            "id": 1712,
            "title": "Business Community’s Hopes for New PM"
        },
        {
            "id": 1713,
            "title": "Agri-Food Challenge Launched to Spur Innovation in Battambang"
        },
        {
            "id": 1714,
            "title": "Siem Reap to Host World Cashew Conference 2024"
        },
        {
            "id": 1715,
            "title": "Warnings Issued Over Money Laundering and Tax Evasion"
        },
        {
            "id": 1716,
            "title": "Vietnam Car Maker Begins Build for North Carolina Electric Vehicle Plant"
        },
        {
            "id": 1717,
            "title": "Post-Pandemic Insights on Financial Management Strategies"
        },
        {
            "id": 1718,
            "title": "South Korean Dog Meat Farmers Push Back Against Growing Moves to Outlaw their Industry"
        },
        {
            "id": 1719,
            "title": "First Cambodian Female AFC Referee"
        },
        {
            "id": 1720,
            "title": "Suspended Garment Workers Receive Fifth Payout"
        },
        {
            "id": 1721,
            "title": "Chea Serey Becomes First Female NBC Governor"
        },
        {
            "id": 1722,
            "title": "The ‘Barbie’ Bonanza Continues at the Box Office, ‘Oppenheimer’ Holds the No. 2 Spot"
        },
        {
            "id": 1723,
            "title": "China Restricts Civilian Drone Exports, Citing Ukraine And Concern About Military Use"
        },
        {
            "id": 1724,
            "title": "Podcast Aims to Connect with Cambodians Living Abroad"
        },
        {
            "id": 1725,
            "title": "Economy On the Mend, Though Risks Remain"
        },
        {
            "id": 1726,
            "title": "Chatbots Sometimes Make Things Up. Not Everyone Thinks AI's Hallucination Problem is Fixable"
        },
        {
            "id": 1727,
            "title": "Fuel Price Hike Sparks Concern Among Drivers"
        },
        {
            "id": 1728,
            "title": "Singer Coco Lee Mourned by Fans and Family at Hong Kong Funeral"
        },
        {
            "id": 1729,
            "title": "Things to do in Siem Reap Away from Angkor"
        },
        {
            "id": 1730,
            "title": "Indonesia Buys 12 Drones Worth $300 Million from Turkey"
        },
        {
            "id": 1731,
            "title": "Climate Change Ravages 11 Roads in Cambodia"
        },
        {
            "id": 1732,
            "title": "Book Explores Youth Identity and Connection to Arts and Culture"
        },
        {
            "id": 1733,
            "title": "RFI Khmer MD Steps Down After Three Decades"
        },
        {
            "id": 1734,
            "title": "The First Generation of Solar Panels Will Wear Out. A Recycling Industry is Taking Shape"
        },
        {
            "id": 1735,
            "title": "Why are Gas Prices Rising? Experts Point to Extreme Heat and Oil Production Cuts"
        },
        {
            "id": 1736,
            "title": "IFC Watchman Starts Probe into Six MFIs"
        },
        {
            "id": 1737,
            "title": "$460m Road Officially Inaugurated"
        },
        {
            "id": 1738,
            "title": "Volunteerism: A Tool to Elevate Society"
        },
        {
            "id": 1739,
            "title": "Three Looted Cambodian Antiquities to be Returned in 2026"
        },
        {
            "id": 1740,
            "title": "Eight Fisheries Receive Food Safety Certification"
        },
        {
            "id": 1741,
            "title": "US Urged to Renew GSP"
        },
        {
            "id": 1742,
            "title": "Explainer: How to Boost DigitalTech in Cambodia"
        },
        {
            "id": 1743,
            "title": "Three Cambodian Films to be Screened at International Film Festivals"
        },
        {
            "id": 1744,
            "title": "Crafting Quality Handmade Cambodian Shoes"
        },
        {
            "id": 1745,
            "title": "China Proposes to Limit Children's Smartphone Time to a Maximum of 2 Hours a Day"
        },
        {
            "id": 1746,
            "title": "A Cyberattack Has Disrupted Hospitals and Health Care in Several States"
        },
        {
            "id": 1747,
            "title": "Roadmap to Cambodia’s EnergyTech Future"
        },
        {
            "id": 1748,
            "title": "King Officially Appoints Hun Manet as Next PM"
        },
        {
            "id": 1749,
            "title": "Cambodian Girl Dreams of Starting a Vehicle Manufacturing Company"
        },
        {
            "id": 1750,
            "title": "Younger Generation of Leaders Mark New Era for Cambodia"
        },
        {
            "id": 1751,
            "title": "Cambodian Movie Scoops Award at Regional Film Festival"
        },
        {
            "id": 1752,
            "title": "Dungeons & Dragons Tells Illustrators to Stop Using AI to Generate Artwork for Fantasy Franchise"
        },
        {
            "id": 1753,
            "title": "People Are Losing More Money To Scammers Than Ever Before. Here's How To Keep Yourself Safe"
        },
        {
            "id": 1754,
            "title": "Preservation of Khmer Culture in the US"
        },
        {
            "id": 1755,
            "title": "Koh Pich Night Market Proves Popular with Vendors and Visitors"
        },
        {
            "id": 1756,
            "title": "Apple Pay Debuts in Vietnam"
        },
        {
            "id": 1757,
            "title": "Merger with Kookmin Sees Prasac Upgraded to Commercial Bank Status"
        },
        {
            "id": 1758,
            "title": "ASEAN-Cambodia Business Summit Promotes Economic Integration"
        },
        {
            "id": 1759,
            "title": "MoT Demands Apology from “Uncle Roger” After Cambodian Food Comment"
        },
        {
            "id": 1760,
            "title": "Tycoon Hy Kimhong Arrested During Dramatic Police Operation"
        },
        {
            "id": 1761,
            "title": "Four Cambodian Fishery Products to be Sold in China"
        },
        {
            "id": 1762,
            "title": "Company Hit with Two-Week Suspension for River Pollution"
        },
        {
            "id": 1763,
            "title": "Wall Street Drops With Markets Worldwide On Worries About Banks And The Economy"
        },
        {
            "id": 1764,
            "title": "Credit Loss Allowance Sinks ACLEDA’s Net Profit by 31.5% in Q2’23"
        },
        {
            "id": 1765,
            "title": "Zoom Says It Isn't Training AI On Calls Without Consent. But Other Data Is Fair Game"
        },
        {
            "id": 1766,
            "title": "WeWork Warns There's 'Substantial Doubt' About Its Ability To Stay In Business"
        },
        {
            "id": 1767,
            "title": "The Rise of Cambodia’s Most Influential Food Blogger"
        },
        {
            "id": 1768,
            "title": "Cambodia’s Indigenous Youth Transforming Communities"
        },
        {
            "id": 1769,
            "title": "Power of Art Embraced to Advocate Change in Battambang"
        },
        {
            "id": 1770,
            "title": "MEF Holds Forum on Non-sovereign Loans"
        },
        {
            "id": 1771,
            "title": "Inquiry Ordered into Suicides Relating to Rattanakiri Debt Collection"
        },
        {
            "id": 1772,
            "title": "Tycoon Denies Defraud to Police"
        },
        {
            "id": 1773,
            "title": "Profit at Japan's Honda Doubles on Healthy Global Auto and Motorcycle Sales"
        },
        {
            "id": 1774,
            "title": "Sony's Profits Drop as It Warns of the Impact From US Movie Strikes"
        },
        {
            "id": 1775,
            "title": "Tiny Toones Calls for Donation for the Future of Vulnerable Kids"
        },
        {
            "id": 1776,
            "title": "Finance Flagged as Biggest Challenge for Businesses to Invest in Tech"
        },
        {
            "id": 1777,
            "title": "Suspended Factory Workers Face Daily Struggle"
        },
        {
            "id": 1778,
            "title": "Cambodia’s Current Account Deficit Falls Sharply in Q1’23"
        },
        {
            "id": 1779,
            "title": "Cambodia Reveals New Generation of Ministers"
        },
        {
            "id": 1780,
            "title": "Losses of $21m Filed Against Tycoon, Hy Kimhong"
        },
        {
            "id": 1781,
            "title": "Paper Exams, Chatbot Bans: Colleges Seek to 'ChatGPT-proof' Assignments"
        },
        {
            "id": 1782,
            "title": "Journalists Seek Regulations to Govern Fast-moving Artificial Intelligence Technology"
        },
        {
            "id": 1783,
            "title": "Chinese Foreign Minister to Pay Official Visit to Cambodia"
        },
        {
            "id": 1784,
            "title": "PPSP Posts Net Profit, Higher Revenue on Land Sales in Q2’23"
        },
        {
            "id": 1785,
            "title": "Worldcoin Scans Eyeballs and Offers Crypto. What to Know about the Project from OpenAI's CEO"
        },
        {
            "id": 1786,
            "title": "Cambodia’s Indigenous People Celebrated"
        },
        {
            "id": 1787,
            "title": "Paddy Prices Experience Unprecedented Rise"
        },
        {
            "id": 1788,
            "title": "Sihanoukville Port’s Q2 Profit Down 33% on Lower Forex Gains"
        },
        {
            "id": 1789,
            "title": "PWSA Net Profit Drained on Rising Finance Costs, Income Tax"
        },
        {
            "id": 1790,
            "title": "Cellcard Owner CAMGSM Takes Out $112.5m Term Loans"
        },
        {
            "id": 1791,
            "title": "Stimulating FDI to Strengthen Cambodia’s Economy"
        },
        {
            "id": 1792,
            "title": "Fiction Writers Fear the Rise of AI, But Also See It As a Story to Tell"
        },
        {
            "id": 1793,
            "title": "MJQE’s Q2 Net Profit, Revenue up on Tuition Fee Growth"
        },
        {
            "id": 1794,
            "title": "Incubation to Promote Climate Resilient Agriculture"
        },
        {
            "id": 1795,
            "title": "Drive Towards an EV Nation"
        },
        {
            "id": 1796,
            "title": "Cambodia Pushes for Investment Hub Status in ASEAN"
        },
        {
            "id": 1797,
            "title": "Toxic Blister Beetles Kill Four"
        },
        {
            "id": 1798,
            "title": "Crackdown on Illegal Import of Piranhas Launched"
        },
        {
            "id": 1799,
            "title": "Garment Maker GTI Doubles Net Profit in Q2’23"
        },
        {
            "id": 1800,
            "title": "Cambodia Aims to Position Itself as A Solo Destination for Tourists"
        },
        {
            "id": 1801,
            "title": "For Mark Zuckerberg's Threads, the Real Rival Is Still TikTok — Not the Former Twitter"
        },
        {
            "id": 1802,
            "title": "Ford Lures Apple Executive to Oversee Its New Software Subscription Services Unit"
        },
        {
            "id": 1803,
            "title": "Is Cambodia Ready to Embrace Generative AI in Education?"
        },
        {
            "id": 1804,
            "title": "Mondulkiri Students Learn About Digital Literacy"
        },
        {
            "id": 1805,
            "title": "CPAs Nurture Livelihoods and Landscapes"
        },
        {
            "id": 1806,
            "title": "Alleged Victims of Kampot Land Fraud Speak Out"
        },
        {
            "id": 1807,
            "title": "App Showcases Cambodia’s Ecotourism Gems"
        },
        {
            "id": 1808,
            "title": "Thinking of Buying a New Pair of Jeans? Breaking Down the Cost Over Time Might Help You Decide"
        },
        {
            "id": 1809,
            "title": "Asia Shares Decline As Faltering Chinese Economy Sets Off Global Slide"
        },
        {
            "id": 1810,
            "title": "Falling Cargo Throughput Impacts PPAP’s Q2 Earnings"
        },
        {
            "id": 1811,
            "title": "ACLEDA Borrows $80m from SinoPac to Fund MSMEs"
        },
        {
            "id": 1812,
            "title": "Pestech Suffers $5.7m Net Loss in FY’23"
        },
        {
            "id": 1813,
            "title": "MoE Rolls Out Measures to Control Disposal of Unsafe Meat"
        },
        {
            "id": 1814,
            "title": "Hun Manet Speaks Out Against Legalizing Marijuana"
        },
        {
            "id": 1815,
            "title": "Bond Issuer PPC Bank Net Profit up 43% in Q2"
        },
        {
            "id": 1816,
            "title": "Hun Sen Takes to State-Owned Media to Thank China For Support"
        },
        {
            "id": 1817,
            "title": "Indonesia Burns Marijuana Plantation That Was Discovered By Drones"
        },
        {
            "id": 1818,
            "title": "Workers Lose Out on Six Public Holidays in 2024"
        },
        {
            "id": 1819,
            "title": "Stakeholders Aim to Elevate Cambodia’s Food Standards"
        },
        {
            "id": 1820,
            "title": "Negotiations for Garment Workers’ Pay Rise Get Underway"
        },
        {
            "id": 1821,
            "title": "AP, Other News Organizations Develop Standards for Use of Artificial Intelligence in Newsrooms"
        },
        {
            "id": 1822,
            "title": "Royal Group Settles Largest Debt of $723m After 12 Years"
        },
        {
            "id": 1823,
            "title": "A $5.4 Billion International Chip Deal with Intel Is off after Greenlight from China Never Arrives"
        },
        {
            "id": 1824,
            "title": "Parents Demand Unhealthy Food Ban in Schools"
        },
        {
            "id": 1825,
            "title": "Singapore Police Seize $83M Assets in Money Laundering Ring Involving Cambodians"
        },
        {
            "id": 1826,
            "title": "Thai Company to Open $100M Oil Depot in Cambodia"
        },
        {
            "id": 1827,
            "title": "Indonesia Increases Cambodian Rice Imports"
        },
        {
            "id": 1828,
            "title": "NYC Bans Use of TikTok on City-owned Phones, Joining Federal Government, Majority of States"
        },
        {
            "id": 1829,
            "title": "Investment Scams Are Everywhere on Social Media. Here's How to Spot One"
        },
        {
            "id": 1830,
            "title": "China's Xi Calls for Measures to Mitigate Disastrous Flooding amid Cconomic Slowdown"
        },
        {
            "id": 1831,
            "title": "TV Drama ‘Sok San Family’ Returns for Second Season"
        },
        {
            "id": 1832,
            "title": "Can GDT Meet Tax Revenue Target Despite Global Headwinds?"
        },
        {
            "id": 1833,
            "title": "GDT  Raises Taxes on Non-alcoholic Beverages"
        },
        {
            "id": 1834,
            "title": "Vann Molyvann Provides Inspiration for Cambodia’s Future Architects"
        },
        {
            "id": 1835,
            "title": "Malaysia Condemns Comedian’s Criticism of Cambodian Food"
        },
        {
            "id": 1836,
            "title": "Lifelike Robots and Android Dogs Wow Visitors at Beijing Robotics Fair: AP PHOTOS"
        },
        {
            "id": 1837,
            "title": "Using the Business Model Canvas to Design a Solid Business Plan"
        },
        {
            "id": 1838,
            "title": "Emerging Economies Are Pushing to End the Dollar's Dominance. But What's the Alternative?"
        },
        {
            "id": 1839,
            "title": "Cyberattack Keeps Hospitals' Computers Offline for Weeks"
        },
        {
            "id": 1840,
            "title": "Launching A Hand-Made Candle Business"
        },
        {
            "id": 1841,
            "title": "Caring for Mental Health"
        },
        {
            "id": 1842,
            "title": "PropertyGuru Awards Celebrate Cambodia’s Real Estate Success"
        },
        {
            "id": 1843,
            "title": "San Francisco Launches Driverless Bus Service Following Robotaxi Expansion"
        },
        {
            "id": 1844,
            "title": "Generative AI: The Next Big Thing for Businesses, But With Risks"
        },
        {
            "id": 1845,
            "title": "Parliament Convene First Plenary Session"
        },
        {
            "id": 1846,
            "title": "Phnom Penh's Busy Coffee Stand"
        },
        {
            "id": 1847,
            "title": "Financial Literacy is Key to Keep Real Estate Market Afloat"
        },
        {
            "id": 1848,
            "title": "Global Food Security Is at Crossroads as Rice Shortages and Surging Prices Hit the Most Vulnerable"
        },
        {
            "id": 1849,
            "title": "White House Science Adviser Calls for More Safeguards Against Artificial Intelligence Risks"
        },
        {
            "id": 1850,
            "title": "Cambodia's New Generation of Ministers Officially Approved"
        },
        {
            "id": 1851,
            "title": "QR Code Payments Agreed with Laos"
        },
        {
            "id": 1852,
            "title": "Access to Finance for SMEs in Cambodia"
        },
        {
            "id": 1853,
            "title": "Boost Capital Raises $2.5M to Accelerate Growth and Transform Digital Banking"
        },
        {
            "id": 1854,
            "title": "John Warnock, Who Helped Invent the PDF and Co-founded Adobe Systems, Dies at Age 82"
        },
        {
            "id": 1855,
            "title": "Digital Technology Adoption by Cambodia’s Tourism MSMEs"
        },
        {
            "id": 1856,
            "title": "US Ambassador Commits to Ties with Cambodia"
        },
        {
            "id": 1857,
            "title": "Cambodia’s CPI in June up Year-on-Year"
        },
        {
            "id": 1858,
            "title": "Work Plan Aims to Help Cambodia Hit Mine-Free Target by 2025"
        },
        {
            "id": 1859,
            "title": "Europe's Sweeping Rules for Tech Giants Are about to Kick in. Here's How They Work"
        },
        {
            "id": 1860,
            "title": "CADT to Host a Developer Conference"
        },
        {
            "id": 1861,
            "title": "Public Concerns Raised Over Food Safety"
        },
        {
            "id": 1862,
            "title": "Digital Clones and Vocaloids May Be Popular in Japan"
        },
        {
            "id": 1863,
            "title": "Tablet Hand Soap Business Aims to Reduce Plastic"
        },
        {
            "id": 1864,
            "title": "IBM Is Selling The Weather Company Assets to Private Equity Firm Francisco Partners"
        },
        {
            "id": 1865,
            "title": "Xi, Putin and other Leaders Locked in Discussions over an Expansion of the BRICS Economic Bloc"
        },
        {
            "id": 1866,
            "title": "Hun Manet Lays Out Future Vision for Cambodia"
        },
        {
            "id": 1867,
            "title": "Cambodia's Digital Journey Shows Signs of Growth"
        },
        {
            "id": 1868,
            "title": "Post-Covid Effects, the Fed’s Interest Rates Grip Cambodian Banks"
        },
        {
            "id": 1869,
            "title": "Starbucks' Pumpkin Spice Latte Turns 20, Beloved by Millions and Despised by Some"
        },
        {
            "id": 1870,
            "title": "Founders of Crypto Mixer Arrested, Sanctioned after US Cracks Down on Tornado Cash"
        },
        {
            "id": 1871,
            "title": "Nvidia's Rising Star Gets even Brighter with another Stellar Quarter Propelled by Sales of AI Chips"
        },
        {
            "id": 1872,
            "title": "ABA and ACLEDA Dominate Cambodia’s Banking Sector"
        },
        {
            "id": 1873,
            "title": "Paddy Price Increase’s Impacts on Rice Sector"
        },
        {
            "id": 1874,
            "title": "Europe Is Cracking Down on Big Tech. This Is What Will Change When You Sign on"
        },
        {
            "id": 1875,
            "title": "Popular ‘Sok San Family’ Second Season Premieres"
        },
        {
            "id": 1876,
            "title": "Festival Raises Awareness of Diversity"
        },
        {
            "id": 1877,
            "title": "‘Change Make Her’ Offers Financial Aid to 45,000 Entrepreneurs"
        },
        {
            "id": 1878,
            "title": "Explainer: How Content Creators Can Promote Cambodia's Tourism Industry"
        },
        {
            "id": 1879,
            "title": "Breastfeeding Rates in Cambodia at “Alarming” Decline"
        },
        {
            "id": 1880,
            "title": "India's Lunar Rover Goes down a Ramp to the Moon's Surface and Takes a Walk"
        },
        {
            "id": 1881,
            "title": "Economy's Solid Growth Could Require More Fed Hikes to Fight Inflation, Powell Says"
        },
        {
            "id": 1882,
            "title": "Cultivating Vanilla to Innovate Cambodia’s Agriculture"
        },
        {
            "id": 1883,
            "title": "Herbal Tea Boosts Health and Farmers’ Income"
        },
        {
            "id": 1884,
            "title": "Students Turn to Vapes to Relieve Stress"
        },
        {
            "id": 1885,
            "title": "Cambodian Students Look Ahead to Science"
        },
        {
            "id": 1886,
            "title": "Children’s Environmental Health Assessment Flags Risks"
        },
        {
            "id": 1887,
            "title": "ABC Reserve Unveils New Tall Can"
        },
        {
            "id": 1888,
            "title": "Study Explores Garment Workers’ Transition to Digital Wages"
        },
        {
            "id": 1889,
            "title": "Minimum Wage Negotiations for Factory Workers Continue"
        },
        {
            "id": 1890,
            "title": "Fisherman Nets Juvenile Crocodile"
        },
        {
            "id": 1891,
            "title": "Early Apple Computer that Helped Launch $3T Company Sells at Auction for $223,000"
        },
        {
            "id": 1892,
            "title": "How PayPal is Using AI to Combat Fraud, and Make it Easier to Pay"
        },
        {
            "id": 1893,
            "title": "Community Libraries Bridging the Knowledge Gap"
        },
        {
            "id": 1894,
            "title": "DMC Students Showcase their Film Skills"
        },
        {
            "id": 1895,
            "title": "Ezecom: Powering Cambodia's Digital Journey in the SEA Games"
        },
        {
            "id": 1896,
            "title": "Tracing Pour un Sourire d’Enfant’s 25 Years Work with Dumpsite Children in Phnom Penh"
        },
        {
            "id": 1897,
            "title": "Advocating for LGBTQI Rights in the Face of Adversity"
        },
        {
            "id": 1898,
            "title": "Hun Manet Lays Out Policies to Improve Garment Workers’ Living Standard"
        },
        {
            "id": 1899,
            "title": "OCIC Group, Best Real Estate Developer 2023, to Launch New Mixed-Use Waterfront Projects"
        },
        {
            "id": 1901,
            "title": "Low Income Bites Into Street Vendor’s Ability to Access Healthcare via NSSF"
        },
        {
            "id": 1902,
            "title": "Spurt in Eco-friendly Startups Seen in Cambodia"
        },
        {
            "id": 1903,
            "title": "No Task Too Big for Intellectually-disabled Residents of Damnok Toek in Kep"
        },
        {
            "id": 1904,
            "title": "Global Inflation Pressures Could Become Harder to Manage in Coming Years, Research Suggests"
        },
        {
            "id": 1905,
            "title": "ECB's Lagarde Says Interest Rates to Stay High as Long as Needed to Defeat Inflation"
        },
        {
            "id": 1906,
            "title": "Up to $100m Allocated for Agri Sector to Support Farmers"
        },
        {
            "id": 1907,
            "title": "No 60CC Bike Licence Requirement, Only a Study for Now"
        },
        {
            "id": 1908,
            "title": "NBC Prepares to Intervene Following Rise in Exchange Rate"
        },
        {
            "id": 1909,
            "title": "Phare Instills the Love of Reading In Rural Children in Battambang"
        },
        {
            "id": 1910,
            "title": "Prahok Prices Rise and Sales Slump As Cost of Local Fish Increases"
        },
        {
            "id": 1911,
            "title": "UNICEF and China are Piloting Climate-Durable WASH Technology in Cambodia"
        },
        {
            "id": 1912,
            "title": "Report Unveils Extent of Online Scamming in SEA"
        },
        {
            "id": 1913,
            "title": "Standardised Loan Contracts for New Loans"
        },
        {
            "id": 1914,
            "title": "“Unacceptable Sacrifices” Made by Kampong Speu Borrowers to Repay Loans"
        },
        {
            "id": 1915,
            "title": "Culture Above Politics: US and Cambodia Extend Cultural Heritage Agreement"
        },
        {
            "id": 1916,
            "title": "Cambodian Health Tech Company Registers in US to Expand Global Reach"
        },
        {
            "id": 1917,
            "title": "Fighting for the Rights of Cambodians with Disabilities"
        },
        {
            "id": 1918,
            "title": "Producing Healthy Products from Local Farmers"
        },
        {
            "id": 1919,
            "title": "Navigating Online Business Registration: A Step-by-Step Guide"
        },
        {
            "id": 1920,
            "title": "India is One of the World's Fastest-growing EV Markets. This Is Why"
        },
        {
            "id": 1921,
            "title": "Thai Police Say Man Kills His Family after Online Scam Leaves Them in Massive Debt"
        },
        {
            "id": 1922,
            "title": "China's Baidu Makes AI Chatbot Ernie Bot Publicly Available"
        },
        {
            "id": 1923,
            "title": "Visual Artists Fight Back Against AI Companies for Repurposing their Work"
        },
        {
            "id": 1924,
            "title": "Agri-tech: The Future of Farming in Cambodia"
        },
        {
            "id": 1925,
            "title": "Berk Chet Festival Heads to Phnom Penh"
        },
        {
            "id": 1926,
            "title": "Unlocking Key Factors to Raise Funds from Investors"
        },
        {
            "id": 1927,
            "title": "JS Land Sees Wider Net Loss in Q2"
        },
        {
            "id": 1928,
            "title": "Southeast Asia Globe to Suspend Operations"
        },
        {
            "id": 1929,
            "title": "Royal Railway Stays in Red in Q2"
        },
        {
            "id": 1930,
            "title": "Amala Aims to Empower Women About Menstruation"
        },
        {
            "id": 1931,
            "title": "Taylor Swift Eras Tour Concert Film Coming to Movie Theaters in October"
        },
        {
            "id": 1932,
            "title": "Children Hit Hardest by the Pandemic are Now the Big Kids at School. Many Still Need Reading Help"
        },
        {
            "id": 1933,
            "title": "New York Police Will Use Drones to Monitor Backyard Parties this Weekend, Spurring Privacy Concerns"
        },
        {
            "id": 1934,
            "title": "Billionaires Want to Build a New City in Rural California"
        },
        {
            "id": 1935,
            "title": "Farmers Face Challenges in Growing Safe Vegetables"
        },
        {
            "id": 1936,
            "title": "India's Moon Rover Completes its Walk, Scientists Analyzing Data Looking for Signs of Frozen Water."
        },
        {
            "id": 1937,
            "title": "Crafting Role Models in Comic Form"
        },
        {
            "id": 1938,
            "title": "SATCHA: A Sustainable Business Model for Promoting Local Crafts in Cambodia"
        },
        {
            "id": 1939,
            "title": "Rise in Suicides Attributed to Burden of Personal Debt"
        },
        {
            "id": 1940,
            "title": "Southeast Asian Leaders Are Besieged by Thorny Issues as They Hold an ASEAN Summit without Biden"
        },
        {
            "id": 1941,
            "title": "ASEAN Summit to See Youngest Cambodian PM in 20 Years"
        },
        {
            "id": 1942,
            "title": "Measures Needed to Cater to People with Disabilities in Workplace"
        },
        {
            "id": 1943,
            "title": "$8.4m Project Pumped into Coastal Communities"
        },
        {
            "id": 1944,
            "title": "Berk Chet Festival Hailed A Success"
        },
        {
            "id": 1945,
            "title": "NBC to Auction $50m in Four Stages"
        },
        {
            "id": 1946,
            "title": "New Class of Asia 21 Next Generation Fellows Named"
        },
        {
            "id": 1947,
            "title": "CCIM Executive Director Resigns"
        },
        {
            "id": 1948,
            "title": "Four Astronauts Return to Earth in SpaceX Capsule to Wrap up Six-month Station Mission"
        },
        {
            "id": 1949,
            "title": "China's Xi Will Skip G20 Summit in India during a Period of Soured Bilateral Relations"
        },
        {
            "id": 1950,
            "title": "Call to Slash Passport Prices"
        },
        {
            "id": 1951,
            "title": "Minimum Wage of $215 Requested for Garment Workers"
        },
        {
            "id": 1952,
            "title": "An Orangutan, Chirping Birds and a Waterfall at ASEAN Venue Contrast to Jakarta's Pollution Outside"
        },
        {
            "id": 1953,
            "title": "PSE to Host Fundraising Birthday Bash for its Founder"
        },
        {
            "id": 1954,
            "title": "Hun Manet Youngest Leader at ASEAN Summit"
        },
        {
            "id": 1955,
            "title": "MCFA Urges Halt Use of Deceptive Photos to Flog Artefacts"
        },
        {
            "id": 1956,
            "title": "Black Soldier Fly Larvae to Address Organic Waste Management"
        },
        {
            "id": 1957,
            "title": "350 Tourism Businesses Receive $54.16m"
        },
        {
            "id": 1958,
            "title": "Prosecutors in All 50 States Urge Congress to Strengthen Tools to Fight AI Child Sexual Abuse Images"
        },
        {
            "id": 1959,
            "title": "TikTok's Irish Data Center up and Running as European Privacy Project Gets under Way"
        },
        {
            "id": 1960,
            "title": "Information Theft Is on the Rise. People Are Particularly Vulnerable after Natural Disasters"
        },
        {
            "id": 1961,
            "title": "What is Green Hydrogen and Why Is It Touted as a Clean Fuel?"
        },
        {
            "id": 1962,
            "title": "Cambodia Post to Auction Unidentified Goods to Help Children's Hospital"
        },
        {
            "id": 1963,
            "title": "Development in the Capital Fuels Traffic Woes"
        },
        {
            "id": 1964,
            "title": "MoU Inked with Philippines to Raise Cambodia’s Farming"
        },
        {
            "id": 1965,
            "title": "Garment Workers to Receive Up to $40 Monthly Compensation"
        },
        {
            "id": 1966,
            "title": "Banks Financed Climate Crisis and Clearing of Indigenous Land"
        },
        {
            "id": 1967,
            "title": "Chea Suon Bopha Continues Father's Legacy of Providing Rest Stops for Travelers"
        },
        {
            "id": 1968,
            "title": "China Exports Decline Slower than Expected in August as Weak Demand Keeps Economy under Pressure"
        },
        {
            "id": 1969,
            "title": "Japan Launches Rocket Carrying Lunar Lander and X-ray Telescope to Explore Origins of Universe"
        },
        {
            "id": 1970,
            "title": "Australia Orders 10 Containers of Fragrant Rice"
        },
        {
            "id": 1971,
            "title": "Need to Curate “Green Premium” Tourism Experiences"
        },
        {
            "id": 1972,
            "title": "Friend Music School Takes on Challenges to Elevate Music Education"
        },
        {
            "id": 1973,
            "title": "Food Safety Program Launched to Combat Food Poisoning"
        },
        {
            "id": 1974,
            "title": "Heineken Cambodia Appoints Andy Hewson as New Managing Director"
        },
        {
            "id": 1975,
            "title": "GDP to Grow at 5.8% on Tourism Growth but Exports Dim"
        },
        {
            "id": 1976,
            "title": "Urbanland Partners with Phillip Trustee to Facilitate Foreign Homebuyers at Borey Chankiri"
        },
        {
            "id": 1977,
            "title": "PM’s Policy Continuity Implies Low Short-term Political Risk"
        },
        {
            "id": 1978,
            "title": "‘One Village, One Product’ Event Promotes Local Products in Banteay Meanchey"
        },
        {
            "id": 1979,
            "title": "Artificial Intelligence Technology Behind ChatGPT Was Built in Iowa — with a Lot of Water"
        },
        {
            "id": 1980,
            "title": "Art Initiative Aims to Transform Kep into Cultural Hub"
        },
        {
            "id": 1981,
            "title": "Unlocking Key Knowledge, Execution, and Legal Safeguards to Raise Funds"
        },
        {
            "id": 1982,
            "title": "Keeping the Tradition of Apsara Alive"
        },
        {
            "id": 1983,
            "title": "Phnom Penh Port’s Container Throughput Down in August, But Rest of the Segments Hold up"
        },
        {
            "id": 1984,
            "title": "Biden Says US Outreach to Vietnam Is about Providing Global Stability, Not Containing China"
        },
        {
            "id": 1985,
            "title": "Circus Promotes Arts and Education"
        },
        {
            "id": 1986,
            "title": "Residents Hospitalized by Ice Factory Gas Leak"
        },
        {
            "id": 1987,
            "title": "Transforming Kep into A High-End Beach Destination"
        },
        {
            "id": 1988,
            "title": "Motor-Mocha Coffee - A Young Couple’s Investment in Cambodia’s Coffee-Drinking Culture"
        },
        {
            "id": 1989,
            "title": "Weekend Software Development Event Draws Thousands"
        },
        {
            "id": 1990,
            "title": "Sweden Brings More Books and Handwriting Practice Back to Its Tech-heavy Schools"
        },
        {
            "id": 1991,
            "title": "Empowering Youths To Collaborate Over Sustainable Climate Action"
        },
        {
            "id": 1992,
            "title": "Farmers’ Profits Hit by Further Drop in Paddy Prices"
        },
        {
            "id": 1994,
            "title": "It's Google Versus the US in the Biggest Antitrust Trial in Decades"
        },
        {
            "id": 1995,
            "title": "Cycling to Raise Funds for Cambodian Children"
        },
        {
            "id": 1996,
            "title": "Nurturing Cambodia’s Entrepreneur Ecosystem"
        },
        {
            "id": 1997,
            "title": "Chicken Farmer Quits Degree to Meet Rising Demand"
        },
        {
            "id": 1998,
            "title": "MDI Deposits Up 9% at 170 Trillion Riel in H1"
        },
        {
            "id": 1999,
            "title": "Apple Set to Unveil the iPhone 15. Here’s What to Expect"
        },
        {
            "id": 2000,
            "title": "Apple's New iPhones Get Faster Chips, Better Cameras and New Charging Ports"
        },
        {
            "id": 2001,
            "title": "Turning Trash into Commodities"
        },
        {
            "id": 2002,
            "title": "Plan to Develop Sustainable Cities"
        },
        {
            "id": 2003,
            "title": "Waste Management Essential in Rural Cambodia"
        },
        {
            "id": 2004,
            "title": "Providing Health Care to the People"
        },
        {
            "id": 2005,
            "title": "33 Looted Ancient Khmer Artifacts Return Home"
        },
        {
            "id": 2006,
            "title": "Angkor Scholar Dr Damian Evans Dies"
        },
        {
            "id": 2007,
            "title": "Game Injects Fun into Learning"
        },
        {
            "id": 2008,
            "title": "One for One Book Exchange Project Promotes Literacy"
        },
        {
            "id": 2009,
            "title": "What is USB-C, the Charging Socket that Replaced Apple's Lightning Cable?"
        },
        {
            "id": 2010,
            "title": "International Literacy Day Celebrations Promote Lifelong Learning"
        },
        {
            "id": 2011,
            "title": "Cross Border Payments, A Boon for Cambodians"
        },
        {
            "id": 2012,
            "title": "Riel Hackathon for Kids Equips Students With Financial Literacy Skills"
        },
        {
            "id": 2013,
            "title": "CAMFOOD & CAMHOTEL 2023 Promotes F&B and Hospitality Sectors"
        },
        {
            "id": 2014,
            "title": "Cambodia Signs $787m Concessional Loans in Six Months"
        },
        {
            "id": 2015,
            "title": "Championing Female Football"
        },
        {
            "id": 2016,
            "title": "Phnom Penh Port’s August, 8-month revenue down"
        },
        {
            "id": 2017,
            "title": "RCEP: A Boon for Cambodia's Economy, but Challenges Remain"
        },
        {
            "id": 2018,
            "title": "Business Registration Requirements Relaxed for Informal Workers"
        },
        {
            "id": 2019,
            "title": "Cambodia and China Sign 15 MoUs and Pledge Mutual Support"
        },
        {
            "id": 2020,
            "title": "Koh Ker Achieves World Heritage Site Status"
        },
        {
            "id": 2021,
            "title": "Dutch Grievance Unit to Examine Oikocredit’s Link with MFI Human Rights Abuse"
        },
        {
            "id": 2022,
            "title": "CAMGSM PLC Q2 Report of Financial Year 2023 Reveals Robust Performance and Financial Position"
        },
        {
            "id": 2023,
            "title": "Telco major CamGSM reports $11m net profit in Q2"
        },
        {
            "id": 2024,
            "title": "ACLEDA Plans $100m Thai baht-bond Listing in Thailand"
        },
        {
            "id": 2025,
            "title": "How Tieng Sophea Uses Google Products to Attract Foreign Visitors"
        },
        {
            "id": 2026,
            "title": "Flights Diverted Due to Severe Storms in Phnom Penh"
        },
        {
            "id": 2027,
            "title": "US Embassy Week Starts in Banteay Meanchey"
        },
        {
            "id": 2028,
            "title": "Capital Gains Tax Takes Effect Jan 1, 2024 Onwards"
        },
        {
            "id": 2029,
            "title": "Instacart Sets IPO Price at $30 a Share, Valuing the Company at about $10 Billion"
        },
        {
            "id": 2030,
            "title": "Four Primary School Pupils Bag Title with Traditional Khmer Dessert Idea"
        },
        {
            "id": 2031,
            "title": "Promote Khmer Culture Art Through Drawing"
        },
        {
            "id": 2032,
            "title": "Cambodia’s GDP Growth Challenged by External Risks, AMRO"
        },
        {
            "id": 2033,
            "title": "Concerns Over AI’s Potential to Cut Jobs"
        },
        {
            "id": 2034,
            "title": "Recycling Batteries to Support A Cleaner Cambodia"
        },
        {
            "id": 2035,
            "title": "PM Raises Concerns Over Future Support of Children"
        },
        {
            "id": 2036,
            "title": "Students Awarded for Innovation"
        },
        {
            "id": 2037,
            "title": "ADB Downgrades GDP Forecast, Risks Plague Outlook"
        },
        {
            "id": 2038,
            "title": "GDT Issues Reminder for Taxpayers to Declare Unused Land Tax"
        },
        {
            "id": 2039,
            "title": "Cambodia Rice Meets Thai and Vietnam Demand as Global Price Spikes"
        },
        {
            "id": 2040,
            "title": "Traditional Dance and Drums Celebrate Koh Ker’s UNESCO Crown"
        },
        {
            "id": 2041,
            "title": "US Calls on Cambodians to Buy American Goods"
        },
        {
            "id": 2042,
            "title": "MFI Funder to Consult with Dutch NCP over Unethical Lending Complaints"
        },
        {
            "id": 2043,
            "title": "Explainer: How to Prevent Facebook Hacking"
        },
        {
            "id": 2044,
            "title": "Exhibit Explores Impact of Construction on Nature and Humans"
        },
        {
            "id": 2045,
            "title": "Reduced Electricity Bills for Agricultural and Industrial Sectors"
        },
        {
            "id": 2046,
            "title": "Chinese Officials Voice Faith in Economy and Keep Interest Rates Steady as Forecasts Darken"
        },
        {
            "id": 2048,
            "title": "First Cambodian Dried Fish Producer With a Disability Achieves CQS"
        },
        {
            "id": 2049,
            "title": "Organizations Urge Media to Increase Breastfeeding Coverage"
        },
        {
            "id": 2050,
            "title": "Cost of Fuel Jumps Again"
        },
        {
            "id": 2051,
            "title": "Coconut Farmers Can Export Produce to China"
        },
        {
            "id": 2052,
            "title": "Tech Companies Try to Take AI Image Generators Mainstream with Better Protections Against Misuse"
        },
        {
            "id": 2053,
            "title": "Eco-Friendly Products for Environmentally-Friendly Lifestyles"
        },
        {
            "id": 2054,
            "title": "ABA Named Best Digital Bank in Cambodia 2023, Confirming its Dedication to Digital Innovation"
        },
        {
            "id": 2055,
            "title": "Direct Flights to Resume Between Cambodia and Japan"
        },
        {
            "id": 2056,
            "title": "International Day of Peace​ Promotes Peaceful Coexistence"
        },
        {
            "id": 2057,
            "title": "Producing Quality Khmer Sausages"
        },
        {
            "id": 2058,
            "title": "Awards Reward Sustainable Business Practices"
        },
        {
            "id": 2059,
            "title": "Battling Discrimination As a Female Tuk Tuk Driver"
        },
        {
            "id": 2060,
            "title": "Smart Unveils ‘Smart for Business’ – a Game-Changer for Companies in the Digital Age"
        },
        {
            "id": 2061,
            "title": "Australia Pledges Support to Cambodia’s Agri-food SMEs"
        },
        {
            "id": 2062,
            "title": "Report Reveals 160,000 Children Sexually Abused or Exploited Online"
        },
        {
            "id": 2063,
            "title": "Cambodia Quality Seal Boosts Food Safety in Fisheries Processing Sector"
        },
        {
            "id": 2064,
            "title": "Banking Loans Rise 11% to $58b from January to June"
        },
        {
            "id": 2065,
            "title": "Designing a Local Brand to Take on International Players"
        },
        {
            "id": 2066,
            "title": "ASEAN-Cambodia Business Summit Promotes Economic Integration"
        },
        {
            "id": 2067,
            "title": "Updated Cambodian Dictionary Published"
        },
        {
            "id": 2068,
            "title": "“One for One” Book Exchange Launches Online Platform"
        },
        {
            "id": 2069,
            "title": "Government Urged to Improve Draft Personal Data Protection Law"
        },
        {
            "id": 2070,
            "title": "Koh Kong Port Launches Testing Operations"
        },
        {
            "id": 2071,
            "title": "Solving Phnom Penh’s Traffic Requires a Multi-Faceted Approach"
        },
        {
            "id": 2072,
            "title": "GPAC Hold International Day of Peace Celebrations"
        },
        {
            "id": 2073,
            "title": "ADB Signs $140m Loan Agreement to Boost Skills and Public Services"
        },
        {
            "id": 2074,
            "title": "Understanding Cambodia's Capital Gains Tax: What You Need to Know"
        },
        {
            "id": 2075,
            "title": "Almost 75,000 Dogs Receive Rabies Vaccination"
        },
        {
            "id": 2076,
            "title": "Incubation Program Aims to Empower Cambodia's Future"
        },
        {
            "id": 2077,
            "title": "Opportunities and Challenges for Cambodia’s Tourism Sector"
        },
        {
            "id": 2078,
            "title": "Cambodia YIGF Raises Youth Awareness on Internet Governance"
        },
        {
            "id": 2079,
            "title": "Concerns Mount Over Health Supplement False Claims"
        },
        {
            "id": 2080,
            "title": "Pestech Sees Red in FY’23, With $5.7m Net Loss"
        },
        {
            "id": 2081,
            "title": "Report Reveals Stark Findings for Garment Workers"
        },
        {
            "id": 2082,
            "title": "Challenging Road to Extend NSSF Benefits"
        },
        {
            "id": 2083,
            "title": "AMK Customers Can Transfer to Visa Cards Worldwide"
        },
        {
            "id": 2086,
            "title": "GDT Rejects “Misleading” Information Spread About CGT"
        },
        {
            "id": 2087,
            "title": "US Ambassador Meets PM to Tighten Relations"
        },
        {
            "id": 2088,
            "title": "Investment Opportunities Highlighted in Cambodian-French Chamber’s Second Edition of Business Guide"
        },
        {
            "id": 2089,
            "title": "Australia and Cambodia Promote Gender Equality Within Industry and MSMEs"
        },
        {
            "id": 2090,
            "title": "Delegation Assess Impact of CAPFISH Program in Tonle Sap"
        },
        {
            "id": 2091,
            "title": "Designing Quality Spaces to Enhance Lifestyles"
        },
        {
            "id": 2092,
            "title": "World's First DIB Delivers $10m to Improve Sanitation"
        },
        {
            "id": 2093,
            "title": "PM Still Mulling Conditions of CGT"
        },
        {
            "id": 2094,
            "title": "New Thai PM Makes First Official Visit to Cambodia"
        },
        {
            "id": 2095,
            "title": "EuroCham and AHK Vietnam Unite to Increase German Investment"
        },
        {
            "id": 2096,
            "title": "Using AI in Education"
        },
        {
            "id": 2097,
            "title": "Garment Workers' Monthly Wage to Increase by $4 in 2024"
        },
        {
            "id": 2098,
            "title": "S&P Global’s “CreditWatch” Ratings on Nagaworld’s NagaCorp Retained"
        },
        {
            "id": 2099,
            "title": "PM Signs Sub-decree To Slash Export Tax on Natural Stone Products"
        },
        {
            "id": 2100,
            "title": "Construction of Big C Hypermaket Set to Start"
        },
        {
            "id": 2101,
            "title": "Largest Esports Tournament To Take Over AEON 2"
        },
        {
            "id": 2102,
            "title": "Street Tour Gives Tourists Glimpse Into Local Life"
        },
        {
            "id": 2103,
            "title": "Art Home Fosters a Family-like Experience for Tourists"
        },
        {
            "id": 2104,
            "title": "Exhibition Celebrates Stories Behind the Canvas"
        },
        {
            "id": 2105,
            "title": "Heineken's \"Worlds Together\" Campaign Brings together Community Gatherings"
        }
    ]

# target_title = "Chea Serey Becomes First Female NBC Governor"
target_title = "Chea Serey Becomes First Female NBC Governor"
# titles = ["Title 1", "Title 2", "Title 3", "Title 4"]
titles = [article['title'] for article in all_articles]

# Preprocess titles
def preprocess(text):
    # Tokenize, lemmatize, and remove stopwords
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

preprocessed_target = preprocess(target_title)
preprocessed_titles = [preprocess(title) for title in titles]

print(f'-----> preprocessed_target: {preprocessed_target}')

# Vectorize titles
target_vector = nlp(preprocessed_target).vector
title_vectors = [nlp(title).vector for title in preprocessed_titles]

print(f'==> target_vector: {target_vector}')

# Calculate cosine similarity
similarities = [np.dot(target_vector, vector) / (np.linalg.norm(target_vector) * np.linalg.norm(vector)) for vector in title_vectors]
print(f'=> similarity: {similarities}')

# Define a similarity threshold (adjust as needed)
threshold = 0.75
# Find related articles
related_articles = [titles[i] for i, sim in enumerate(similarities) if sim > threshold]

print("Related Articles:")
for article in related_articles:
    print(article)
