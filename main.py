import webview

def create_app():
    # Gemini ওয়েবসাইট লোড করা
    window = webview.create_window(
        'Gemini AI - Rasel Mia', 
        'https://gemini.google.com',
        width=1200, 
        height=800,
        resizable=True
    )
    webview.start()

if __name__ == '__main__':
    create_app()\documentclass[11pt, a4paper, oneside]{book}

% --- UNIVERSAL PREAMBLE BLOCK ---
\usepackage[a4paper, top=2.5cm, bottom=2.5cm, left=2cm, right=2cm]{geometry}
\usepackage{fontspec}

\usepackage[bengali, bidi=basic, provide=*]{babel}

\babelprovide[import, onchar=ids fonts]{bengali}
\babelprovide[import, onchar=ids fonts]{english}

% Set default/Latin font to Sans Serif in the main (rm) slot
\babelfont{rm}{Noto Sans}
% Assign a specific font for Bengali text
\babelfont[bengali]{rm}{Noto Sans Bengali}

\usepackage{enumitem}
\setlist[itemize]{label=-}

% --- STYLING PACKAGES ---
\usepackage{xcolor}
\usepackage{tikz}
\usepackage[many]{tcolorbox}

% --- COLOR DEFINITIONS (Matched with Tailwind CSS) ---
\definecolor{ruleRed}{HTML}{DC2626}
\definecolor{pillDark}{HTML}{27272A}
\definecolor{bgBlue}{HTML}{EFF6FF}
\definecolor{borderBlue}{HTML}{DBEAFE}
\definecolor{textBlue}{HTML}{1D4ED8}
\definecolor{textDark}{HTML}{1F2937}

% --- CUSTOM COMMANDS FOR UI BLOCKS ---

% 1. Command for the Rule Header (Red Circle + Dark Pill)
\newcommand{\ruleheader}[3]{%
    \vspace*{2em}\noindent
    \begin{tikzpicture}
        % Pill Background
        \node[
            fill=pillDark, 
            text=white, 
            rounded corners=15pt, 
            right, 
            minimum height=1.8cm, 
            text width=\textwidth-2.5cm, 
            inner xsep=25pt
        ] (box) at (0.9cm, 0) {
            {\large\bfseries #2}\\[0.3em]
            {\Large\bfseries #3}
        };
        % Red Number Circle
        \node[
            circle, 
            fill=ruleRed, 
            text=white, 
            minimum size=1.8cm, 
            font=\Large\bfseries, 
            draw=white, 
            line width=2pt
        ] at (0.9cm, 0) {#1};
    \end{tikzpicture}\par\vspace*{1em}
}

% 2. Environment for the Examples Box (Light Blue Background)
\newtcolorbox{examplebox}{
    enhanced,
    breakable,
    colback=bgBlue,
    colframe=borderBlue,
    boxrule=1pt,
    arc=10pt,
    title={\textcolor{textBlue}{\Large\bfseries Examples (উদাহরণ)}},
    coltitle=textBlue,
    colbacktitle=bgBlue,
    titlerule=1pt,
    titlerule style={borderBlue},
    bottomtitle=1ex,
    toptitle=1ex,
    left=10pt, right=10pt, top=10pt, bottom=10pt,
    boxsep=0pt
}

% 3. Command for Individual Example Items (White Box)
\newcommand{\exampleitem}[2]{%
    \begin{tcolorbox}[
        enhanced,
        breakable=false,
        colback=white,
        colframe=black!10,
        boxrule=0.5pt,
        arc=5pt,
        top=6pt, bottom=6pt, left=10pt, right=10pt,
        boxsep=0pt
    ]
        {\normalsize\bfseries \color{textDark} #1} \\[0.3em]
        {\normalsize\bfseries \color{textBlue} #2}
    \end{tcolorbox}
}


\begin{document}

% --- TITLE ---
\begin{center}
    {\Huge \bfseries \textcolor{textBlue}{English Mastery}}\\[0.5em]
    {\Large \bfseries \textcolor{gray}{200 Rules Step-by-Step}}
\end{center}
\vspace{1em}

% ==========================================
% RULE 01
% ==========================================
\ruleheader{01.}{আমি একজন শিক্ষার্থী।}{I am a student.}

\begin{examplebox}
    \exampleitem{১. আমি একজন শিক্ষক।}{1. I am a teacher.}
    \exampleitem{২. সে একজন ডাক্তার।}{2. He is a doctor.}
    \exampleitem{৩. তারা খেলোয়াড়।}{3. They are players.}
    \exampleitem{৪. তুমি একজন গায়ক।}{4. You are a singer.}
    \exampleitem{৫. আমরা বন্ধু।}{5. We are friends.}
    \exampleitem{৬. রিনা একজন নার্স।}{6. Rina is a nurse.}
    \exampleitem{৭. সে একজন কৃষক।}{7. He is a farmer.}
    \exampleitem{৮. আপনি একজন লেখক।}{8. You are a writer.}
    \exampleitem{৯. তারা ছাত্র।}{9. They are students.}
    \exampleitem{১০. আমি একজন পাইলট।}{10. I am a pilot.}
\end{examplebox}


% ==========================================
% RULE 02
% ==========================================
\ruleheader{02.}{আমি বাংলাদেশে আছি।}{I am in Bangladesh.}

\begin{examplebox}
    \exampleitem{১. আমি অফিসে আছি।}{1. I am in the office.}
    \exampleitem{২. সে বাড়িতে আছে।}{2. He is at home.}
    \exampleitem{৩. তারা মাঠে আছে।}{3. They are in the field.}
    \exampleitem{৪. তুমি স্কুলে আছো।}{4. You are at school.}
    \exampleitem{৫. আমরা মিটিংয়ে আছি।}{5. We are in a meeting.}
    \exampleitem{৬. রিনা বাজারে আছে।}{6. Rina is in the market.}
    \exampleitem{৭. বাবা ঢাকায় আছেন।}{7. Father is in Dhaka.}
    \exampleitem{৮. মা রান্নাঘরে আছেন।}{8. Mother is in the kitchen.}
    \exampleitem{৯. বইটি টেবিলে আছে।}{9. The book is on the table.}
    \exampleitem{১০. গাড়িটি রাস্তায় আছে।}{10. The car is on the road.}
\end{examplebox}


% ==========================================
% RULE 03
% ==========================================
\ruleheader{03.}{আমি একজন শিক্ষার্থী ছিলাম।}{I was a student.}

\begin{examplebox}
    \exampleitem{১. আমি একজন শিক্ষক ছিলাম।}{1. I was a teacher.}
    \exampleitem{২. সে একজন ডাক্তার ছিল।}{2. He was a doctor.}
    \exampleitem{৩. তারা খেলোয়াড় ছিল।}{3. They were players.}
    \exampleitem{৪. তুমি একজন গায়ক ছিলে।}{4. You were a singer.}
    \exampleitem{৫. আমরা বন্ধু ছিলাম।}{5. We were friends.}
    \exampleitem{৬. রিনা একজন নার্স ছিল।}{6. Rina was a nurse.}
    \exampleitem{৭. সে একজন কৃষক ছিল।}{7. He was a farmer.}
    \exampleitem{৮. আপনি একজন লেখক ছিলেন।}{8. You were a writer.}
    \exampleitem{৯. তারা ছাত্র ছিল।}{9. They were students.}
    \exampleitem{১০. আমি একজন পাইলট ছিলাম।}{10. I was a pilot.}
\end{examplebox}


% ==========================================
% RULE 04
% ==========================================
\ruleheader{04.}{আমি বাংলাদেশে ছিলাম।}{I was in Bangladesh.}

\begin{examplebox}
    \exampleitem{১. আমি অফিসে ছিলাম।}{1. I was in the office.}
    \exampleitem{২. সে বাড়িতে ছিল।}{2. He was at home.}
    \exampleitem{৩. তারা মাঠে ছিল।}{3. They were in the field.}
    \exampleitem{৪. তুমি স্কুলে ছিলে।}{4. You were at school.}
    \exampleitem{৫. আমরা মিটিংয়ে ছিলাম।}{5. We are in a meeting.}
    \exampleitem{৬. রিনা বাজারে ছিল।}{6. Rina is in the market.}
    \exampleitem{৭. বাবা ঢাকায় ছিলেন।}{7. Father was in Dhaka.}
    \exampleitem{৮. মা রান্নাঘরে ছিলেন।}{8. Mother was in the kitchen.}
    \exampleitem{৯. বইটি টেবিলে ছিল।}{9. The book was on the table.}
    \exampleitem{১০. গাড়িটি রাস্তায় ছিল।}{10. The car was on the road.}
\end{examplebox}
% ==========================================
% RULE 05
% ==========================================
\ruleheader{05.}{আমি একজন শিক্ষার্থী হবো।}{I will be a student.}

\begin{examplebox}
    \exampleitem{১. আমি একজন ডাক্তার হবো।}{1. I will be a doctor.}
    \exampleitem{২. সে একজন শিক্ষক হবে।}{2. He will be a teacher.}
    \exampleitem{৩. তারা খেলোয়াড় হবে।}{3. They will be players.}
    \exampleitem{৪. তুমি একজন গায়ক হবে।}{4. You will be a singer.}
    \exampleitem{৫. আমরা বন্ধু হবো।}{5. We will be friends.}
    \exampleitem{৬. রিনা একজন নার্স হবে।}{6. Rina will be a nurse.}
    \exampleitem{৭. সে একজন কৃষক হবে।}{7. He will be a farmer.}
    \exampleitem{৮. আপনি একজন লেখক হবেন।}{8. You will be a writer.}
    \exampleitem{৯. তারা ছাত্র হবে।}{9. They will be students.}
    \exampleitem{১০. আমি একজন পাইলট হবো।}{10. I will be a pilot.}
\end{examplebox}

% ==========================================
% RULE 06
% ==========================================
\ruleheader{06.}{আমি বাংলাদেশে থাকবো।}{I will be in Bangladesh.}

\begin{examplebox}
    \exampleitem{১. আমি অফিসে থাকবো।}{1. I will be in the office.}
    \exampleitem{২. সে বাড়িতে থাকবে।}{2. He will be at home.}
    \exampleitem{৩. তারা মাঠে থাকবে।}{3. They will be in the field.}
    \exampleitem{৪. তুমি স্কুলে থাকবে।}{4. You will be at school.}
    \exampleitem{৫. আমরা মিটিংয়ে থাকবো।}{5. We will be in a meeting.}
    \exampleitem{৬. রিনা বাজারে থাকবে।}{6. Rina will be in the market.}
    \exampleitem{৭. বাবা ঢাকায় থাকবেন।}{7. Father will be in Dhaka.}
    \exampleitem{৮. মা রান্নাঘরে থাকবেন।}{8. Mother will be in the kitchen.}
    \exampleitem{৯. বইটি টেবিলে থাকবে।}{9. The book will be on the table.}
    \exampleitem{১০. গাড়িটি রাস্তায় থাকবে।}{10. The car will be on the road.}
\end{examplebox}

% ==========================================
% RULE 07
% ==========================================
\ruleheader{07.}{আমার একজন শিক্ষার্থী আছে।}{I have a student.}

\begin{examplebox}
    \exampleitem{১. আমার একটি ল্যাপটপ আছে।}{1. I have a laptop.}
    \exampleitem{২. তার একটি গাড়ি আছে।}{2. He has a car.}
    \exampleitem{৩. তাদের একটি বাগান আছে।}{3. They have a garden.}
    \exampleitem{৪. তোমার একটি সুন্দর হাসি আছে।}{4. You have a beautiful smile.}
    \exampleitem{৫. আমাদের একটি সমস্যা আছে।}{5. We have a problem.}
    \exampleitem{৬. রিনার একটি বিড়াল আছে।}{6. Rina has a cat.}
    \exampleitem{৭. তার অনেক টাকা আছে।}{7. He has a lot of money.}
    \exampleitem{৮. আপনার একটি ভালো ধারণা আছে।}{8. You have a good idea.}
    \exampleitem{৯. তাদের অনেক সময় আছে।}{9. They have a lot of time.}
    \exampleitem{১০. আমার একটি বই আছে।}{10. I have a book.}
\end{examplebox}

% ==========================================
% RULE 08
% ==========================================
\ruleheader{08.}{আমার একজন শিক্ষার্থী ছিল।}{I had a student.}

\begin{examplebox}
    \exampleitem{১. আমার একটি সাইকেল ছিল।}{1. I had a bicycle.}
    \exampleitem{২. তার একটি মোবাইল ছিল।}{2. He had a mobile.}
    \exampleitem{৩. তাদের একটি বড় বাড়ি ছিল।}{3. They had a big house.}
    \exampleitem{৪. তোমার একটি ভালো সুযোগ ছিল।}{4. You had a good opportunity.}
    \exampleitem{৫. আমাদের অনেক বন্ধু ছিল।}{5. We had many friends.}
    \exampleitem{৬. রিনার একটি কুকুর ছিল।}{6. Rina had a dog.}
    \exampleitem{৭. তার একটি ভালো চাকরি ছিল।}{7. He had a good job.}
    \exampleitem{৮. আপনার একটি সুন্দর স্বপ্ন ছিল।}{8. You had a beautiful dream.}
    \exampleitem{৯. তাদের অনেক ক্ষমতা ছিল।}{9. They had a lot of power.}
    \exampleitem{১০. আমার একটি ঘড়ি ছিল।}{10. I had a watch.}
\end{examplebox}

% ==========================================
% RULE 09
% ==========================================
\ruleheader{09.}{আমার একজন শিক্ষার্থী থাকবে।}{I will have a student.}

\begin{examplebox}
    \exampleitem{১. আমার একটি গাড়ি থাকবে।}{1. I will have a car.}
    \exampleitem{২. তার একটি ল্যাপটপ থাকবে।}{2. He will have a laptop.}
    \exampleitem{৩. তাদের একটি নিজস্ব বাড়ি থাকবে।}{3. They will have their own house.}
    \exampleitem{৪. তোমার অনেক টাকা থাকবে।}{4. You will have a lot of money.}
    \exampleitem{৫. আমাদের একটি সুন্দর ভবিষ্যৎ থাকবে।}{5. We will have a beautiful future.}
    \exampleitem{৬. রিনার একটি ভালো চাকরি থাকবে।}{6. Rina will have a good job.}
    \exampleitem{৭. তার অনেক বন্ধু থাকবে।}{7. He will have many friends.}
    \exampleitem{৮. আপনার একটি সফল ব্যবসা থাকবে।}{8. You will have a successful business.}
    \exampleitem{৯. তাদের অনেক সুযোগ থাকবে।}{9. They will have many opportunities.}
    \exampleitem{১০. আমার একটি নতুন ফোন থাকবে।}{10. I will have a new phone.}
\end{examplebox}

% ==========================================
% RULE 10
% ==========================================
\ruleheader{10.}{আমাদের বাড়িতে একজন শিক্ষার্থী আছে।}{There is a student in our home.}

\begin{examplebox}
    \exampleitem{১. আমাদের গ্রামে একটি স্কুল আছে।}{1. There is a school in our village.}
    \exampleitem{২. ঘরে একটি টেবিল আছে।}{2. There is a table in the room.}
    \exampleitem{৩. মাঠে একটি গাছ আছে।}{3. There is a tree in the field.}
    \exampleitem{৪. পুকুরে একটি মাছ আছে।}{4. There is a fish in the pond.}
    \exampleitem{৫. আকাশে একটি চাঁদ আছে।}{5. There is a moon in the sky.}
    \exampleitem{৬. বাগানে একটি ফুল আছে।}{6. There is a flower in the garden.}
    \exampleitem{৭. পকেটে একটি কলম আছে।}{7. There is a pen in the pocket.}
    \exampleitem{৮. শহরে একটি হাসপাতাল আছে।}{8. There is a hospital in the city.}
    \exampleitem{৯. গ্লাসে একটি চামচ আছে।}{9. There is a spoon in the glass.}
    \exampleitem{১০. ব্যাগে একটি বই আছে।}{10. There is a book in the bag.}
\end{examplebox}
% ==========================================
% RULE 11
% ==========================================
\ruleheader{11.}{আমাদের বাড়িতে একজন শিক্ষার্থী ছিল।}{There was a student in our home.}

\begin{examplebox}
    \exampleitem{১. আমাদের গ্রামে একটি স্কুল ছিল।}{1. There was a school in our village.}
    \exampleitem{২. ঘরে একটি টেবিল ছিল।}{2. There was a table in the room.}
    \exampleitem{৩. মাঠে একটি গাছ ছিল।}{3. There was a tree in the field.}
    \exampleitem{৪. পুকুরে একটি মাছ ছিল।}{4. There was a fish in the pond.}
    \exampleitem{৫. আকাশে একটি চাঁদ ছিল।}{5. There was a moon in the sky.}
    \exampleitem{৬. বাগানে একটি ফুল ছিল।}{6. There was a flower in the garden.}
    \exampleitem{৭. পকেটে একটি কলম ছিল।}{7. There was a pen in the pocket.}
    \exampleitem{৮. শহরে একটি হাসপাতাল ছিল।}{8. There was a hospital in the city.}
    \exampleitem{৯. গ্লাসে একটি চামচ ছিল।}{9. There was a spoon in the glass.}
    \exampleitem{১০. ব্যাগে একটি বই ছিল।}{10. There was a book in the bag.}
\end{examplebox}

% ==========================================
% RULE 12
% ==========================================
\ruleheader{12.}{আমাদের বাড়িতে একজন শিক্ষার্থী থাকবে।}{There will be a student in our home.}

\begin{examplebox}
    \exampleitem{১. আমাদের গ্রামে একটি স্কুল থাকবে।}{1. There will be a school in our village.}
    \exampleitem{২. ঘরে একটি টেবিল থাকবে।}{2. There will be a table in the room.}
    \exampleitem{৩. মাঠে একটি গাছ থাকবে।}{3. There will be a tree in the field.}
    \exampleitem{৪. পুকুরে একটি মাছ থাকবে।}{4. There will be a fish in the pond.}
    \exampleitem{৫. আকাশে একটি চাঁদ থাকবে।}{5. There will be a moon in the sky.}
    \exampleitem{৬. বাগানে একটি ফুল থাকবে।}{6. There will be a flower in the garden.}
    \exampleitem{৭. পকেটে একটি কলম থাকবে।}{7. There will be a pen in the pocket.}
    \exampleitem{৮. শহরে একটি হাসপাতাল থাকবে।}{8. There will be a hospital in the city.}
    \exampleitem{৯. গ্লাসে একটি চামচ থাকবে।}{9. There will be a spoon in the glass.}
    \exampleitem{১০. ব্যাগে একটি বই থাকবে।}{10. There will be a book in the bag.}
\end{examplebox}

% ==========================================
% RULE 13
% ==========================================
\ruleheader{13.}{আমি ইংরেজিতে কথা বলি।}{I speak English.}

\begin{examplebox}
    \exampleitem{১. আমি বাংলা শিখি।}{1. I learn Bengali.}
    \exampleitem{২. সে বই পড়ে।}{2. He reads books.}
    \exampleitem{৩. তারা ফুটবল খেলে।}{3. They play football.}
    \exampleitem{৪. তুমি গান গাও।}{4. You sing a song.}
    \exampleitem{৫. আমরা স্কুলে যাই।}{5. We go to school.}
    \exampleitem{৬. রিনা ছবি আঁকে।}{6. Rina draws a picture.}
    \exampleitem{৭. সে সত্য কথা বলে।}{7. He speaks the truth.}
    \exampleitem{৮. আপনি ভালো কাজ করেন।}{8. You do good work.}
    \exampleitem{৯. তারা আমাকে সাহায্য করে।}{9. They help me.}
    \exampleitem{১০. আমি সকালে হাটি।}{10. I walk in the morning.}
\end{examplebox}

% ==========================================
% RULE 14
% ==========================================
\ruleheader{14.}{আমি ইংরেজিতে কথা বলছি।}{I am speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি বাংলা শিখছি।}{1. I am learning Bengali.}
    \exampleitem{২. সে বই পড়ছে।}{2. He is reading a book.}
    \exampleitem{৩. তারা ফুটবল খেলছে।}{3. They are playing football.}
    \exampleitem{৪. তুমি গান গাইছ।}{4. You are singing a song.}
    \exampleitem{৫. আমরা স্কুলে যাচ্ছি।}{5. We are going to school.}
    \exampleitem{৬. রিনা ছবি আঁকছে।}{6. Rina is drawing a picture.}
    \exampleitem{৭. সে সত্য কথা বলছে।}{7. He is speaking the truth.}
    \exampleitem{৮. আপনি একটি চিঠি লিখছেন।}{8. You are writing a letter.}
    \exampleitem{৯. তারা আমাকে ডাকছে।}{9. They are calling me.}
    \exampleitem{১০. আমি চা পান করছি।}{10. I am drinking tea.}
\end{examplebox}

% ==========================================
% RULE 15
% ==========================================
\ruleheader{15.}{আমি ইংরেজিতে কথা বলেছি।}{I have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করেছি।}{1. I have done the work.}
    \exampleitem{২. সে বইটি পড়েছে।}{2. He has read the book.}
    \exampleitem{৩. তারা ফুটবল খেলেছে।}{3. They have played football.}
    \exampleitem{৪. তুমি গান গেয়েছ।}{4. You have sung a song.}
    \exampleitem{৫. আমরা স্কুলে গিয়েছি।}{5. We have gone to school.}
    \exampleitem{৬. রিনা ছবিটি আঁকিয়েছে।}{6. Rina has drawn the picture.}
    \exampleitem{৭. সে আমাকে বলেছে।}{7. He has told me.}
    \exampleitem{৮. আপনি একটি চিঠি লিখেছেন।}{8. You have written a letter.}
    \exampleitem{৯. তারা আমাকে সাহায্য করেছে।}{9. They have helped me.}
    \exampleitem{১০. আমি তাকে দেখেছি।}{10. I have seen him.}
\end{examplebox}

% ==========================================
% RULE 16
% ==========================================
\ruleheader{16.}{আমি এক ঘণ্টা ধরে ইংরেজিতে কথা বলছি।}{I have been speaking English for an hour.}

\begin{examplebox}
    \exampleitem{১. আমি সকাল থেকে কাজ করছি।}{1. I have been working since morning.}
    \exampleitem{২. সে দুই ঘণ্টা ধরে পড়ছে।}{2. He has been reading for two hours.}
    \exampleitem{৩. তারা বিকেল থেকে খেলছে।}{3. They have been playing since afternoon.}
    \exampleitem{৪. তুমি ১০ মিনিট ধরে কাঁদছ।}{4. You have been crying for 10 minutes.}
    \exampleitem{৫. আমরা তিন বছর ধরে এখানে বাস করছি।}{5. We have been living here for three years.}
    \exampleitem{৬. রিনা সকাল থেকে অপেক্ষা করছে।}{6. Rina has been waiting since morning.}
    \exampleitem{৭. সে পাঁচ বছর ধরে ইংরেজি শিখছে।}{7. He has been learning English for five years.}
    \exampleitem{৮. আপনি সোমবার থেকে চেষ্টা করছেন।}{8. You have been trying since Monday.}
    \exampleitem{৯. তারা দীর্ঘক্ষণ ধরে আলোচনা করছে।}{9. They have been discussing for a long time.}
    \exampleitem{১০. সকাল থেকে বৃষ্টি হচ্ছে।}{10. It has been raining since morning.}
\end{examplebox}

% ==========================================
% RULE 17
% ==========================================
\ruleheader{17.}{আমি ইংরেজিতে কথা বললাম।}{I spoke English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করলাম।}{1. I did the work.}
    \exampleitem{২. সে বইটি পড়ল।}{2. He read the book.}
    \exampleitem{৩. তারা ফুটবল খেলল।}{3. They played football.}
    \exampleitem{৪. তুমি একটি গান গাইলে।}{4. You sang a song.}
    \exampleitem{৫. আমরা স্কুলে গেলাম।}{5. We went to school.}
    \exampleitem{৬. রিনা একটি ছবি আঁকল।}{6. Rina drew a picture.}
    \exampleitem{৭. সে সত্য কথা বলল।}{7. He spoke the truth.}
    \exampleitem{৮. আপনি আমাকে ডাকলেন।}{8. You called me.}
    \exampleitem{৯. তারা আমাকে সাহায্য করল।}{9. They helped me.}
    \exampleitem{১০. আমি তাকে দেখলাম।}{10. I saw him.}
\end{examplebox}

% ==========================================
% RULE 18
% ==========================================
\ruleheader{18.}{আমি ইংরেজিতে কথা বলছিলাম।}{I was speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি বইটি পড়ছিলাম।}{1. I was reading the book.}
    \exampleitem{২. সে ঘুমাচ্ছিল।}{2. He was sleeping.}
    \exampleitem{৩. তারা মাঠে খেলছিল।}{3. They were playing in the field.}
    \exampleitem{৪. তুমি একটি গান গাচ্ছিলে।}{4. You were singing a song.}
    \exampleitem{৫. আমরা টিভি দেখছিলাম।}{5. We were watching TV.}
    \exampleitem{৬. রিনা ছবি আঁকছিল।}{6. Rina was drawing a picture.}
    \exampleitem{৭. সে কাজটি করছিল।}{7. He was doing the work.}
    \exampleitem{৮. আপনি চিঠি লিখছিলেন।}{8. You were writing a letter.}
    \exampleitem{৯. তারা কথা বলছিল।}{9. They were talking.}
    \exampleitem{১০. আমি চা পান করছিলাম।}{10. I was drinking tea.}
\end{examplebox}

% ==========================================
% RULE 19
% ==========================================
\ruleheader{19.}{আমি ইংরেজিতে কথা বলেছিলাম।}{I had spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করেছিলাম।}{1. I had done the work.}
    \exampleitem{২. সে বইটি পড়েছিল।}{2. He had read the book.}
    \exampleitem{৩. তারা ফুটবল খেলেছিল।}{3. They had played football.}
    \exampleitem{৪. তুমি গান গেয়েছিলে।}{4. You had sung a song.}
    \exampleitem{৫. আমরা স্কুলে গিয়েছিলাম।}{5. We had gone to school.}
    \exampleitem{৬. রিনা ছবিটি এঁকেছিল।}{6. Rina had drawn the picture.}
    \exampleitem{৭. সে সত্য কথা বলেছিল।}{7. He had spoken the truth.}
    \exampleitem{৮. আপনি আমাকে জানিয়েছিলেন।}{8. You had informed me.}
    \exampleitem{৯. তারা আমাকে নিমন্ত্রণ করেছিল।}{9. They had invited me.}
    \exampleitem{১০. আমি তাকে দেখেছিলাম।}{10. I had seen him.}
\end{examplebox}

% ==========================================
% RULE 20
% ==========================================
\ruleheader{20.}{আমি এক ঘণ্টা ধরে ইংরেজিতে কথা বলছিলাম।}{I had been speaking English for an hour.}

\begin{examplebox}
    \exampleitem{১. আমি সকাল থেকে কাজ করছিলাম।}{1. I had been working since morning.}
    \exampleitem{২. সে দুই ঘণ্টা ধরে পড়ছিল।}{2. He had been reading for two hours.}
    \exampleitem{৩. তারা বিকেল থেকে খেলছিল।}{3. They had been playing since afternoon.}
    \exampleitem{৪. তুমি ১০ মিনিট ধরে কাঁদছিলে।}{4. You had been crying for 10 minutes.}
    \exampleitem{৫. আমরা তিন বছর ধরে সেখানে বাস করছিলাম।}{5. We had been living there for three years.}
    \exampleitem{৬. রিনা সকাল থেকে অপেক্ষা করছিল।}{6. Rina had been waiting since morning.}
    \exampleitem{৭. সে পাঁচ বছর ধরে ইংরেজি শিখছিল।}{7. He had been learning English for five years.}
    \exampleitem{৮. আপনি অনেকক্ষণ ধরে চেষ্টা করছিলেন।}{8. You had been trying for a long time.}
    \exampleitem{৯. তারা দুই ঘণ্টা ধরে কথা বলছিল।}{9. They had been talking for two hours.}
    \exampleitem{১০. সকাল থেকে বৃষ্টি হচ্ছিল।}{10. It had been raining since morning.}
\end{examplebox}
% ==========================================
% RULE 21
% ==========================================
\ruleheader{21.}{আমি ইংরেজিতে কথা বলবো।}{I will speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করবো।}{1. I will do the work.}
    \exampleitem{২. সে স্কুলে যাবে।}{2. He will go to school.}
    \exampleitem{৩. তারা ফুটবল খেলবে।}{3. They will play football.}
    \exampleitem{৪. তুমি একটি গান গাইবে।}{4. You will sing a song.}
    \exampleitem{৫. আমরা তাকে সাহায্য করবো।}{5. We will help him.}
    \exampleitem{৬. রিনা একটি ছবি আঁকবে।}{6. Rina will draw a picture.}
    \exampleitem{৭. সে একটি চিঠি লিখবে।}{7. He will write a letter.}
    \exampleitem{৮. আপনি আমাকে ডাকবেন।}{8. You will call me.}
    \exampleitem{৯. তারা ঢাকা পৌঁছাবে।}{9. They will reach Dhaka.}
    \exampleitem{১০. আমি চা পান করবো।}{10. I will drink tea.}
\end{examplebox}

% ==========================================
% RULE 22
% ==========================================
\ruleheader{22.}{আমি ইংরেজিতে কথা বলতে থাকবো।}{I will be speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি বইটি পড়তে থাকবো।}{1. I will be reading the book.}
    \exampleitem{২. সে ঘুমাতে থাকবে।}{2. He will be sleeping.}
    \exampleitem{৩. তারা মাঠে খেলতে থাকবে।}{3. They will be playing in the field.}
    \exampleitem{৪. তুমি গান গাইতে থাকবে।}{4. You will be singing a song.}
    \exampleitem{৫. আমরা টিভি দেখতে থাকবো।}{5. We will be watching TV.}
    \exampleitem{৬. রিনা ছবি আঁকতে থাকবে।}{6. Rina will be drawing a picture.}
    \exampleitem{৭. সে কাজটি করতে থাকবে।}{7. He will be doing the work.}
    \exampleitem{৮. আপনি চিঠি লিখতে থাকবেন।}{8. You will be writing a letter.}
    \exampleitem{৯. তারা কথা বলতে থাকবে।}{9. They will be talking.}
    \exampleitem{১০. আমি অপেক্ষা করতে থাকবো।}{10. I will be waiting.}
\end{examplebox}

% ==========================================
% RULE 23
% ==========================================
\ruleheader{23.}{আমি ইংরেজিতে কথা বলে থাকবো।}{I will have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করে থাকবো।}{1. I will have done the work.}
    \exampleitem{২. সে বইটি পড়ে থাকবে।}{2. He will have read the book.}
    \exampleitem{৩. তারা ফুটবল খেলে থাকবে।}{3. They will have played football.}
    \exampleitem{৪. তুমি গানটি গেয়ে থাকবে।}{4. You will have sung the song.}
    \exampleitem{৫. আমরা স্কুলে গিয়ে থাকবো।}{5. We will have gone to school.}
    \exampleitem{৬. রিনা ছবিটি এঁকে থাকবে।}{6. Rina will have drawn the picture.}
    \exampleitem{৭. সে সত্য কথা বলে থাকবে।}{7. He will have spoken the truth.}
    \exampleitem{৮. আপনি আমাকে জানিয়ে থাকবেন।}{8. You will have informed me.}
    \exampleitem{৯. তারা স্টেশনে পৌঁছে থাকবে।}{9. They will have reached the station.}
    \exampleitem{১০. আমি তাকে দেখে থাকবো।}{10. I will have seen him.}
\end{examplebox}

% ==========================================
% RULE 24
% ==========================================
\ruleheader{24.}{আমি এক ঘণ্টা ধরে ইংরেজিতে কথা বলতে থাকবো।}{I will have been speaking English for an hour.}

\begin{examplebox}
    \exampleitem{১. আমি সকাল থেকে কাজ করতে থাকবো।}{1. I will have been working since morning.}
    \exampleitem{২. সে দুই ঘণ্টা ধরে পড়তে থাকবে।}{2. He will have been reading for two hours.}
    \exampleitem{৩. তারা বিকেল থেকে খেলতে থাকবে।}{3. They will have been playing since afternoon.}
    \exampleitem{৪. তুমি ১০ মিনিট ধরে কাঁদতে থাকবে।}{4. You will have been crying for 10 minutes.}
    \exampleitem{৫. আমরা তিন বছর ধরে সেখানে বাস করতে থাকবো।}{5. We will have been living there for three years.}
    \exampleitem{৬. রিনা সকাল থেকে অপেক্ষা করতে থাকবে।}{6. Rina will have been waiting since morning.}
    \exampleitem{৭. সে পাঁচ বছর ধরে ইংরেজি শিখতে থাকবে।}{7. He will have been learning English for five years.}
    \exampleitem{৮. আপনি অনেকক্ষণ ধরে চেষ্টা করতে থাকবেন।}{8. You will have been trying for a long time.}
    \exampleitem{৯. তারা দুই ঘণ্টা ধরে কথা বলতে থাকবে।}{9. They will have been talking for two hours.}
    \exampleitem{১০. সকাল থেকে বৃষ্টি হতে থাকবে।}{10. It will have been raining since morning.}
\end{examplebox}

% ==========================================
% RULE 25
% ==========================================
\ruleheader{25.}{আমার ইংরেজিতে কথা বলা উচিৎ।}{I should speak English.}

\begin{examplebox}
    \exampleitem{১. আমার পড়া উচিৎ।}{1. I should read.}
    \exampleitem{২. তার সেখানে যাওয়া উচিৎ।}{2. He should go there.}
    \exampleitem{৩. তাদের খেলা উচিৎ।}{3. They should play.}
    \exampleitem{৪. তোমার তাকে সাহায্য করা উচিৎ।}{4. You should help him.}
    \exampleitem{৫. আমাদের কাজ করা উচিৎ।}{5. We should work.}
    \exampleitem{৬. রিনার ঘুমানো উচিৎ।}{6. Rina should sleep.}
    \exampleitem{৭. তার সত্য কথা বলা উচিৎ।}{7. He should speak the truth.}
    \exampleitem{৮. আপনার বিশ্রাম নেওয়া উচিৎ।}{8. You should take a rest.}
    \exampleitem{৯. তাদের নিয়ম মানা উচিৎ।}{9. They should follow the rules.}
    \exampleitem{১০. আমার চেষ্টা করা উচিৎ।}{10. I should try.}
\end{examplebox}

% ==========================================
% RULE 26
% ==========================================
\ruleheader{26.}{আমার ইংরেজিতে কথা বলতে থাকা উচিৎ।}{I should be speaking English.}

\begin{examplebox}
    \exampleitem{১. আমার পড়তে থাকা উচিৎ।}{1. I should be reading.}
    \exampleitem{২. তার কাজ করতে থাকা উচিৎ।}{2. He should be working.}
    \exampleitem{৩. তাদের খেলতে থাকা উচিৎ।}{3. They should be playing.}
    \exampleitem{৪. তোমার শিখতে থাকা উচিৎ।}{4. You should be learning.}
    \exampleitem{৫. আমাদের হাঁটতে থাকা উচিৎ।}{5. We should be walking.}
    \exampleitem{৬. রিনার বিশ্রাম নিতে থাকা উচিৎ।}{6. Rina should be resting.}
    \exampleitem{৭. তার অপেক্ষা করতে থাকা উচিৎ।}{7. He should be waiting.}
    \exampleitem{৮. আপনার শুনতে থাকা উচিৎ।}{8. You should be listening.}
    \exampleitem{৯. তাদের অনুশীলন করতে থাকা উচিৎ।}{9. They should be practicing.}
    \exampleitem{১০. আমার লিখতে থাকা উচিৎ।}{10. I should be writing.}
\end{examplebox}

% ==========================================
% RULE 27
% ==========================================
\ruleheader{27.}{আমার ইংরেজিতে কথা বলা উচিৎ ছিল।}{I should have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমার কাজটি করা উচিৎ ছিল।}{1. I should have done the work.}
    \exampleitem{২. তার সেখানে যাওয়া উচিৎ ছিল।}{2. He should have gone there.}
    \exampleitem{৩. তাদের আমাকে বলা উচিৎ ছিল।}{3. They should have told me.}
    \exampleitem{৪. তোমার তাকে সাহায্য করা উচিৎ ছিল।}{4. You should have helped him.}
    \exampleitem{৫. আমাদের আগে আসা উচিৎ ছিল।}{5. We should have come earlier.}
    \exampleitem{৬. রিনার ছবিটি আঁকা উচিৎ ছিল।}{6. Rina should have drawn the picture.}
    \exampleitem{৭. তার সত্য কথা বলা উচিৎ ছিল।}{7. He should have spoken the truth.}
    \exampleitem{৮. আপনার ওষুধ খাওয়া উচিৎ ছিল।}{8. You should have taken medicine.}
    \exampleitem{৯. তাদের অপেক্ষা করা উচিৎ ছিল।}{9. They should have waited.}
    \exampleitem{১০. আমার বইটি কেনা উচিৎ ছিল।}{10. I should have bought the book.}
\end{examplebox}

% ==========================================
% RULE 28
% ==========================================
\ruleheader{28.}{আমার ইংরেজিতে কথা বলা দরকার।}{I need to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার পড়া দরকার।}{1. I need to read.}
    \exampleitem{২. তার সেখানে যাওয়া দরকার।}{2. He needs to go there.}
    \exampleitem{৩. তাদের টাকা দরকার।}{3. They need money.} % Using 'need' as main verb for variation
    \exampleitem{৪. তোমার বিশ্রাম নেওয়া দরকার।}{4. You need to take a rest.}
    \exampleitem{৫. আমাদের কাজ করা দরকার।}{5. We need to work.}
    \exampleitem{৬. রিনার একটি বই দরকার।}{6. Rina needs a book.}
    \exampleitem{৭. তার ওষুধ খাওয়া দরকার।}{7. He needs to take medicine.}
    \exampleitem{৮. আপনার সাহায্য দরকার।}{8. You need help.}
    \exampleitem{৯. তাদের নিয়ম জানা দরকার।}{9. They need to know the rules.}
    \exampleitem{১০. আমার ঘুমানো দরকার।}{10. I need to sleep.}
\end{examplebox}

% ==========================================
% RULE 29
% ==========================================
\ruleheader{29.}{আমার ইংরেজিতে কথা বলতে থাকা দরকার।}{I need be speaking English.}

\begin{examplebox}
    \exampleitem{১. আমার পড়তে থাকা দরকার।}{1. I need to be reading.}
    \exampleitem{২. তার কাজ করতে থাকা দরকার।}{2. He needs to be working.}
    \exampleitem{৩. তাদের খেলতে থাকা দরকার।}{3. They need to be playing.}
    \exampleitem{৪. তোমার শিখতে থাকা দরকার।}{4. You need to be learning.}
    \exampleitem{৫. আমাদের হাঁটতে থাকা দরকার।}{5. We need to be walking.}
    \exampleitem{৬. রিনার বিশ্রাম নিতে থাকা দরকার।}{6. Rina needs to be resting.}
    \exampleitem{৭. তার অপেক্ষা করতে থাকা দরকার।}{7. He needs to be waiting.}
    \exampleitem{৮. আপনার শুনতে থাকা দরকার।}{8. You need to be listening.}
    \exampleitem{৯. তাদের অনুশীলন করতে থাকা দরকার।}{9. They need to be practicing.}
    \exampleitem{১০. আমার লিখতে থাকা দরকার।}{10. I need to be writing.}
\end{examplebox}

% ==========================================
% RULE 30
% ==========================================
\ruleheader{30.}{আমার ইংরেজিতে কথা দরকার ছিল।}{I need have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমার কাজটি করা দরকার ছিল।}{1. I need have done the work.}
    \exampleitem{২. তার সেখানে যাওয়া দরকার ছিল।}{2. He need have gone there.}
    \exampleitem{৩. তাদের আমাকে বলা দরকার ছিল।}{3. They need have told me.}
    \exampleitem{৪. তোমার তাকে সাহায্য করা দরকার ছিল।}{4. You need have helped him.}
    \exampleitem{৫. আমাদের আগে আসা দরকার ছিল।}{5. We need have come earlier.}
    \exampleitem{৬. রিনার ছবিটি আঁকা দরকার ছিল।}{6. Rina need have drawn the picture.}
    \exampleitem{৭. তার সত্য কথা বলা দরকার ছিল।}{7. He need have spoken the truth.}
    \exampleitem{৮. আপনার ওষুধ খাওয়া দরকার ছিল।}{8. You need have taken medicine.}
    \exampleitem{৯. তাদের অপেক্ষা করা দরকার ছিল।}{9. They need have waited.}
    \exampleitem{১০. আমার বইটি কেনা দরকার ছিল।}{10. I need have bought the book.}
\end{examplebox}

% ==========================================
% RULE 31
% ==========================================
\ruleheader{31.}{আমি অবশ্যই ইংরেজিতে কথা বলবো।}{I must speak English.}

\begin{examplebox}
    \exampleitem{১. আমি অবশ্যই কাজটি করবো।}{1. I must do the work.}
    \exampleitem{২. সে অবশ্যই আসবে।}{2. He must come.}
    \exampleitem{৩. তারা অবশ্যই খেলবে।}{3. They must play.}
    \exampleitem{৪. তুমি অবশ্যই তাকে সাহায্য করবে।}{4. You must help him.}
    \exampleitem{৫. আমরা অবশ্যই যাবো।}{5. We must go.}
    \exampleitem{৬. রিনা অবশ্যই ছবিটি আঁকবে।}{6. Rina must draw the picture.}
    \exampleitem{৭. সে অবশ্যই সত্য কথা বলবে।}{7. He must speak the truth.}
    \exampleitem{৮. আপনি অবশ্যই শুনবেন।}{8. You must listen.}
    \exampleitem{৯. তারা অবশ্যই জিতবে।}{9. They must win.}
    \exampleitem{১০. আমি অবশ্যই চেষ্টা করবো।}{10. I must try.}
\end{examplebox}

% ==========================================
% RULE 32
% ==========================================
\ruleheader{32.}{আমি অবশ্যই ইংরেজিতে কথা বলিয়া / বলে থাকবো।}{I must have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি অবশ্যই কাজটি করে থাকবো।}{1. I must have done the work.}
    \exampleitem{২. সে অবশ্যই পৌঁছে থাকবে।}{2. He must have arrived.}
    \exampleitem{৩. তারা অবশ্যই খবরটি শুনে থাকবে।}{3. They must have heard the news.}
    \exampleitem{৪. তুমি অবশ্যই ভুল করে থাকবে।}{4. You must have made a mistake.}
    \exampleitem{৫. আমরা অবশ্যই তাকে দেখে থাকবো।}{5. We must have seen him.}
    \exampleitem{৬. রিনা অবশ্যই বইটি পড়ে থাকবে।}{6. Rina must have read the book.}
    \exampleitem{৭. সে অবশ্যই টাকা পাঠিয়ে থাকবে।}{7. He must have sent the money.}
    \exampleitem{৮. আপনি অবশ্যই বুঝতে পেরে থাকবেন।}{8. You must have understood.}
    \exampleitem{৯. তারা অবশ্যই ঘুমিয়ে পড়ে থাকবে।}{9. They must have fallen asleep.}
    \exampleitem{১০. আমি অবশ্যই ভুলে গিয়ে থাকবো।}{10. I must have forgotten.}
\end{examplebox}

% ==========================================
% RULE 33
% ==========================================
\ruleheader{33.}{আমাকে ইংরেজিতে কথা বলতে হয়/ বলতে হবে।}{I have to speak English.}

\begin{examplebox}
    \exampleitem{১. আমাকে যেতে হবে।}{1. I have to go.}
    \exampleitem{২. তাকে কাজ করতে হয়।}{2. He has to work.}
    \exampleitem{৩. তাদের প্রতিদিন পড়তে হয়।}{3. They have to study everyday.}
    \exampleitem{৪. তোমাকে সকালে উঠতে হবে।}{4. You have to wake up early.}
    \exampleitem{৫. আমাদের নিয়ম মানতে হবে।}{5. We have to follow the rules.}
    \exampleitem{৬. রিনাকে রান্না করতে হয়।}{6. Rina has to cook.}
    \exampleitem{৭. তাকে সত্য বলতে হবে।}{7. He has to tell the truth.}
    \exampleitem{৮. আপনাকে অপেক্ষা করতে হবে।}{8. You have to wait.}
    \exampleitem{৯. তাদের টাকা দিতে হবে।}{9. They have to pay the money.}
    \exampleitem{১০. আমাকে এখন ঘুমাতে হবে।}{10. I have to sleep now.}
\end{examplebox}

% ==========================================
% RULE 34
% ==========================================
\ruleheader{34.}{আমাকে ইংরেজিতে কথা বলতে হয়েছিল।}{I had to speak English.}

\begin{examplebox}
    \exampleitem{১. আমাকে সেখানে যেতে হয়েছিল।}{1. I had to go there.}
    \exampleitem{২. তাকে অনেক কাজ করতে হয়েছিল।}{2. He had to do a lot of work.}
    \exampleitem{৩. তাদের সারারাত জাগতে হয়েছিল।}{3. They had to stay awake all night.}
    \exampleitem{৪. তোমাকে অপেক্ষা করতে হয়েছিল।}{4. You had to wait.}
    \exampleitem{৫. আমাদের টাকা ধার করতে হয়েছিল।}{5. We had to borrow money.}
    \exampleitem{৬. রিনাকে একা থাকতে হয়েছিল।}{6. Rina had to stay alone.}
    \exampleitem{৭. তাকে চাকরি ছাড়তে হয়েছিল।}{7. He had to leave the job.}
    \exampleitem{৮. আপনাকে সত্যিটা মানতে হয়েছিল।}{8. You had to accept the truth.}
    \exampleitem{৯. তাদের বাড়ি বিক্রি করতে হয়েছিল।}{9. They had to sell the house.}
    \exampleitem{১০. আমাকে ওষুধ খেতে হয়েছিল।}{10. I had to take medicine.}
\end{examplebox}

% ==========================================
% RULE 35
% ==========================================
\ruleheader{35.}{আমাকে ইংরেজিতে কথা বলতে হবে।}{I will have to speak English.}

\begin{examplebox}
    \exampleitem{১. আমাকে কাল ঢাকা যেতে হবে।}{1. I will have to go to Dhaka tomorrow.}
    \exampleitem{২. তাকে কাজটি শেষ করতে হবে।}{2. He will have to finish the work.}
    \exampleitem{৩. তাদের নতুন বাড়ি খুঁজতে হবে।}{3. They will have to find a new house.}
    \exampleitem{৪. তোমাকে আরও পড়তে হবে।}{4. You will have to study more.}
    \exampleitem{৫. আমাদের সমস্যাটি সমাধান করতে হবে।}{5. We will have to solve the problem.}
    \exampleitem{৬. রিনাকে ইংরেজি শিখতে হবে।}{6. Rina will have to learn English.}
    \exampleitem{৭. তাকে সত্যিটা বলতে হবে।}{7. He will have to tell the truth.}
    \exampleitem{৮. আপনাকে জরিমানা দিতে হবে।}{8. You will have to pay the fine.}
    \exampleitem{৯. তাদের আবার চেষ্টা করতে হবে।}{9. They will have to try again.}
    \exampleitem{১০. আমাকে একটি ল্যাপটপ কিনতে হবে।}{10. I will have to buy a laptop.}
\end{examplebox}
% ==========================================
% RULE 36
% ==========================================
\ruleheader{36.}{আমি ইংরেজিতে কথা বলতে পারি।}{I can speak English.}

\begin{examplebox}
    \exampleitem{১. আমি সাঁতার কাটতে পারি।}{1. I can swim.}
    \exampleitem{২. সে গাড়ি চালাতে পারে।}{2. He can drive a car.}
    \exampleitem{৩. তারা সমস্যাটি সমাধান করতে পারে।}{3. They can solve the problem.}
    \exampleitem{৪. তুমি আমাকে সাহায্য করতে পারো।}{4. You can help me.}
    \exampleitem{৫. আমরা কাজটি শেষ করতে পারি।}{5. We can finish the work.}
    \exampleitem{৬. রিনা ভালো রান্না করতে পারে।}{6. Rina can cook well.}
    \exampleitem{৭. সে দ্রুত দৌড়াতে পারে।}{7. He can run fast.}
    \exampleitem{৮. আপনি এখানে বসতে পারেন।}{8. You can sit here.}
    \exampleitem{৯. তারা ইংরেজি বুঝতে পারে।}{9. They can understand English.}
    \exampleitem{১০. আমি তোমাকে বিশ্বাস করতে পারি।}{10. I can trust you.}
\end{examplebox}

% ==========================================
% RULE 37
% ==========================================
\ruleheader{37.}{আমি ইংরেজিতে কথা বলে থাকতে পারি।}{I can have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করে থাকতে পারি।}{1. I can have done the work.}
    \exampleitem{২. সে সেখানে গিয়ে থাকতে পারে।}{2. He can have gone there.}
    \exampleitem{৩. তারা খবরটি শুনে থাকতে পারে।}{3. They can have heard the news.}
    \exampleitem{৪. তুমি তাকে দেখে থাকতে পারো।}{4. You can have seen him.}
    \exampleitem{৫. আমরা ভুল করে থাকতে পারি।}{5. We can have made a mistake.}
    \exampleitem{৬. রিনা চিঠিটি লিখে থাকতে পারে।}{6. Rina can have written the letter.}
    \exampleitem{৭. সে টাকা পেয়ে থাকতে পারে।}{7. He can have got the money.}
    \exampleitem{৮. আপনি বইটি কিনে থাকতে পারেন।}{8. You can have bought the book.}
    \exampleitem{৯. তারা পৌঁছে থাকতে পারে।}{9. They can have reached.}
    \exampleitem{১০. আমি পাসওয়ার্ড ভুলে গিয়ে থাকতে পারি।}{10. I can have forgotten the password.}
\end{examplebox}

% ==========================================
% RULE 38
% ==========================================
\ruleheader{38.}{আমি ইংরেজিতে কথা বলতে পারলাম।}{I could speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে পারলাম।}{1. I could do the work.}
    \exampleitem{২. সে আসতে পারল।}{2. He could come.}
    \exampleitem{৩. তারা জিততে পারল।}{3. They could win.}
    \exampleitem{৪. তুমি উত্তর দিতে পারলে।}{4. You could answer.}
    \exampleitem{৫. আমরা তাকে বাঁচাতে পারলাম।}{5. We could save him.}
    \exampleitem{৬. রিনা পরীক্ষায় পাস করতে পারল।}{6. Rina could pass the exam.}
    \exampleitem{৭. সে গাড়ি থামাতে পারল।}{7. He could stop the car.}
    \exampleitem{৮. আপনি আমাকে দেখতে পারলেন।}{8. You could see me.}
    \exampleitem{৯. তারা সিদ্ধান্ত নিতে পারল।}{9. They could make a decision.}
    \exampleitem{১০. আমি সময়মতো পৌঁছাতে পারলাম।}{10. I could reach on time.}
\end{examplebox}

% ==========================================
% RULE 39
% ==========================================
\ruleheader{39.}{আমি ইংরেজিতে কথা বলে থাকতে পারতাম।}{I could have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে পারতাম।}{1. I could have done the work.}
    \exampleitem{২. সে সেখানে যেতে পারতো।}{2. He could have gone there.}
    \exampleitem{৩. তারা ম্যাচটি জিততে পারতো।}{3. They could have won the match.}
    \exampleitem{৪. তুমি আমাকে বলতে পারতে।}{4. You could have told me.}
    \exampleitem{৫. আমরা তাকে সাহায্য করতে পারতাম।}{5. We could have helped him.}
    \exampleitem{৬. রিনা ভালো ফলাফল করতে পারতো।}{6. Rina could have made a good result.}
    \exampleitem{৭. সে সত্য কথা বলতে পারতো।}{7. He could have spoken the truth.}
    \exampleitem{৮. আপনি এখানে আসতে পারতেন।}{8. You could have come here.}
    \exampleitem{৯. তারা টাকা ধার দিতে পারতো।}{9. They could have lent the money.}
    \exampleitem{১০. আমি চিঠিটি পাঠাতে পারতাম।}{10. I could have sent the letter.}
\end{examplebox}

% ==========================================
% RULE 40
% ==========================================
\ruleheader{40.}{আমি ইংরেজিতে কথা বলতে পারবো।}{I will be able to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে পারবো।}{1. I will be able to do the work.}
    \exampleitem{২. সে আসতে পারবে।}{2. He will be able to come.}
    \exampleitem{৩. তারা জিততে পারবে।}{3. They will be able to win.}
    \exampleitem{৪. তুমি শিখতে পারবে।}{4. You will be able to learn.}
    \exampleitem{৫. আমরা সাহায্য করতে পারবো।}{5. We will be able to help.}
    \exampleitem{৬. রিনা রান্না করতে পারবে।}{6. Rina will be able to cook.}
    \exampleitem{৭. সে গাড়ি চালাতে পারবে।}{7. He will be able to drive a car.}
    \exampleitem{৮. আপনি বুঝতে পারবেন।}{8. You will be able to understand.}
    \exampleitem{৯. তারা কাজটি শেষ করতে পারবে।}{9. They will be able to finish the work.}
    \exampleitem{১০. আমি সেখানে যেতে পারবো।}{10. I will be able to go there.}
\end{examplebox}

% ==========================================
% RULE 41
% ==========================================
\ruleheader{41.}{আমি ইংরেজিতে কথা বলতে পারছি।}{I am being able to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে পারছি।}{1. I am being able to do the work.}
    \exampleitem{২. সে শিখতে পারছে।}{2. He is being able to learn.}
    \exampleitem{৩. তারা খেলতে পারছে।}{3. They are being able to play.}
    \exampleitem{৪. তুমি বুঝতে পারছো।}{4. You are being able to understand.}
    \exampleitem{৫. আমরা সাহায্য করতে পারছি।}{5. We are being able to help.}
    \exampleitem{৬. রিনা ঘুমাতে পারছে।}{6. Rina is being able to sleep.}
    \exampleitem{৭. সে হাঁটতে পারছে।}{7. He is being able to walk.}
    \exampleitem{৮. আপনি দেখতে পাচ্ছেন।}{8. You are being able to see.}
    \exampleitem{৯. তারা উত্তর দিতে পারছে।}{9. They are being able to answer.}
    \exampleitem{১০. আমি ইংরেজি পড়তে পারছি।}{10. I am being able to read English.}
\end{examplebox}

% ==========================================
% RULE 42
% ==========================================
\ruleheader{42.}{আমি ইংরেজিতে কথা বলতে পেরেছি।}{I have been able to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি শেষ করতে পেরেছি।}{1. I have been able to finish the work.}
    \exampleitem{২. সে আসতে পেরেছে।}{2. He has been able to come.}
    \exampleitem{৩. তারা জিততে পেরেছে।}{3. They have been able to win.}
    \exampleitem{৪. তুমি উত্তর দিতে পেরেছ।}{4. You have been able to answer.}
    \exampleitem{৫. আমরা তাকে বাঁচাতে পেরেছি।}{5. We have been able to save him.}
    \exampleitem{৬. রিনা পরীক্ষায় পাস করতে পেরেছে।}{6. Rina has been able to pass the exam.}
    \exampleitem{৭. সে গাড়ি থামাতে পেরেছে।}{7. He has been able to stop the car.}
    \exampleitem{৮. আপনি আমাকে দেখতে পেরেছেন।}{8. You have been able to see me.}
    \exampleitem{৯. তারা সিদ্ধান্ত নিতে পেরেছে।}{9. They have been able to make a decision.}
    \exampleitem{১০. আমি সময়মতো পৌঁছাতে পেরেছি।}{10. I have been able to reach on time.}
\end{examplebox}

% ==========================================
% RULE 43
% ==========================================
\ruleheader{43.}{আমি ইংরেজিতে কথা না বলে পারি না।}{I cannot but speak English. / I cannot help speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি না করে পারি না।}{1. I cannot but do the work. / I cannot help doing the work.}
    \exampleitem{২. সে সেখানে না গিয়ে পারে না।}{2. He cannot but go there. / He cannot help going there.}
    \exampleitem{৩. তারা না হেসে পারে না।}{3. They cannot but laugh. / They cannot help laughing.}
    \exampleitem{৪. তুমি সত্যিটা না বলে পারো না।}{4. You cannot but tell the truth. / You cannot help telling the truth.}
    \exampleitem{৫. আমরা তাকে সাহায্য না করে পারি না।}{5. We cannot but help him. / We cannot help helping him.}
    \exampleitem{৬. রিনা না কেঁদে পারে না।}{6. Rina cannot but cry. / Rina cannot help crying.}
    \exampleitem{৭. সে চা না পান করে পারে না।}{7. He cannot but drink tea. / He cannot help drinking tea.}
    \exampleitem{৮. আপনি না ভেবে পারেন না।}{8. You cannot but think. / You cannot help thinking.}
    \exampleitem{৯. তারা না ঘুমিয়ে পারে না।}{9. They cannot but sleep. / They cannot help sleeping.}
    \exampleitem{১০. আমি বইটি না পড়ে পারি না।}{10. I cannot but read the book. / I cannot help reading the book.}
\end{examplebox}

% ==========================================
% RULE 44
% ==========================================
\ruleheader{44.}{আমি ইংরেজিতে কথা না বলে পারলাম না।}{I could not but speak English. / I could not help speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি না করে পারলাম না।}{1. I could not but do the work. / I could not help doing the work.}
    \exampleitem{২. সে সেখানে না গিয়ে পারলো না।}{2. He could not but go there. / He could not help going there.}
    \exampleitem{৩. তারা না হেসে পারলো না।}{3. They could not but laugh. / They could not help laughing.}
    \exampleitem{৪. তুমি সত্যিটা না বলে পারলে না।}{4. You could not but tell the truth. / You could not help telling the truth.}
    \exampleitem{৫. আমরা তাকে সাহায্য না করে পারলাম না।}{5. We could not but help him. / We could not help helping him.}
    \exampleitem{৬. রিনা না কেঁদে পারলো না।}{6. Rina could not but cry. / Rina could not help crying.}
    \exampleitem{৭. সে চা না পান করে পারলো না।}{7. He could not but drink tea. / He could not help drinking tea.}
    \exampleitem{৮. আপনি না ভেবে পারলেন না।}{8. You could not but think. / You could not help thinking.}
    \exampleitem{৯. তারা না ঘুমিয়ে পারলো না।}{9. They could not but sleep. / They could not help sleeping.}
    \exampleitem{১০. আমি বইটি না পড়ে পারলাম না।}{10. I could not but read the book. / I could not help reading the book.}
\end{examplebox}

% ==========================================
% RULE 45
% ==========================================
\ruleheader{45.}{আমি ইংরেজিতে কথা বলতে পারি। (৫০\% সম্ভাবনা)}{I may speak English.}

\begin{examplebox}
    \exampleitem{১. আমি আজ যেতে পারি।}{1. I may go today.}
    \exampleitem{২. সে কাল আসতে পারে।}{2. He may come tomorrow.}
    \exampleitem{৩. তারা জিততে পারে।}{3. They may win.}
    \exampleitem{৪. তুমি পাস করতে পারো।}{4. You may pass.}
    \exampleitem{৫. আমরা কাজটি করতে পারি।}{5. We may do the work.}
    \exampleitem{৬. রিনা রান্না করতে পারে।}{6. Rina may cook.}
    \exampleitem{৭. আজ বৃষ্টি হতে পারে।}{7. It may rain today.}
    \exampleitem{৮. আপনি তাকে দেখতে পারেন।}{8. You may see him.}
    \exampleitem{৯. তারা সাহায্য করতে পারে।}{9. They may help.}
    \exampleitem{১০. আমি বইটি কিনতে পারি।}{10. I may buy the book.}
\end{examplebox}

% ==========================================
% RULE 46
% ==========================================
\ruleheader{46.}{আমি ইংরেজিতে কথা বলে থাকতে পারি।}{I may have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করে থাকতে পারি।}{1. I may have done the work.}
    \exampleitem{২. সে সেখানে গিয়ে থাকতে পারে।}{2. He may have gone there.}
    \exampleitem{৩. তারা খবরটি শুনে থাকতে পারে।}{3. They may have heard the news.}
    \exampleitem{৪. তুমি তাকে দেখে থাকতে পারো।}{4. You may have seen him.}
    \exampleitem{৫. আমরা ভুল করে থাকতে পারি।}{5. We may have made a mistake.}
    \exampleitem{৬. রিনা চিঠিটি লিখে থাকতে পারে।}{6. Rina may have written the letter.}
    \exampleitem{৭. সে টাকা পেয়ে থাকতে পারে।}{7. He may have got the money.}
    \exampleitem{৮. আপনি বইটি কিনে থাকতে পারেন।}{8. You may have bought the book.}
    \exampleitem{৯. তারা পৌঁছে থাকতে পারে।}{9. They may have reached.}
    \exampleitem{১০. আমি পাসওয়ার্ড ভুলে গিয়ে থাকতে পারি।}{10. I may have forgotten the password.}
\end{examplebox}

% ==========================================
% RULE 47
% ==========================================
\ruleheader{47.}{আমি ইংরেজিতে বলতে থাকতে পারি।}{I may be speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি পড়তে থাকতে পারি।}{1. I may be reading.}
    \exampleitem{২. সে ঘুমাতে থাকতে পারে।}{2. He may be sleeping.}
    \exampleitem{৩. তারা খেলতে থাকতে পারে।}{3. They may be playing.}
    \exampleitem{৪. তুমি গান গাইতে থাকতে পারো।}{4. You may be singing.}
    \exampleitem{৫. আমরা অপেক্ষা করতে থাকতে পারি।}{5. We may be waiting.}
    \exampleitem{৬. রিনা কাজ করতে থাকতে পারে।}{6. Rina may be working.}
    \exampleitem{৭. সে ড্রাইভ করতে থাকতে পারে।}{7. He may be driving.}
    \exampleitem{৮. আপনি দেখতে থাকতে পারেন।}{8. You may be watching.}
    \exampleitem{৯. তারা আলোচনা করতে থাকতে পারে।}{9. They may be discussing.}
    \exampleitem{১০. আমি লিখতে থাকতে পারি।}{10. I may be writing.}
\end{examplebox}

% ==========================================
% RULE 48
% ==========================================
\ruleheader{48.}{আমি ইংরেজিতে কথা বলতে পারি। (৩০\% সম্ভাবনা)}{I might speak English.}

\begin{examplebox}
    \exampleitem{১. আমি আজ যেতে পারি।}{1. I might go today.}
    \exampleitem{২. সে কাল আসতে পারে।}{2. He might come tomorrow.}
    \exampleitem{৩. তারা জিততে পারে।}{3. They might win.}
    \exampleitem{৪. তুমি পাস করতে পারো।}{4. You might pass.}
    \exampleitem{৫. আমরা কাজটি করতে পারি।}{5. We might do the work.}
    \exampleitem{৬. রিনা রান্না করতে পারে।}{6. Rina might cook.}
    \exampleitem{৭. আজ বৃষ্টি হতে পারে।}{7. It might rain today.}
    \exampleitem{৮. আপনি তাকে দেখতে পারেন।}{8. You might see him.}
    \exampleitem{৯. তারা সাহায্য করতে পারে।}{9. They might help.}
    \exampleitem{১০. আমি বইটি কিনতে পারি।}{10. I might buy the book.}
\end{examplebox}

% ==========================================
% RULE 49
% ==========================================
\ruleheader{49.}{আমি ইংরেজিতে কথা বলে থাকতে পারতাম।}{I might have spoken English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করে থাকতে পারতাম।}{1. I might have done the work.}
    \exampleitem{২. সে সেখানে গিয়ে থাকতে পারতো।}{2. He might have gone there.}
    \exampleitem{৩. তারা ম্যাচটি জিততে পারতো।}{3. They might have won the match.}
    \exampleitem{৪. তুমি আমাকে বলতে পারতে।}{4. You might have told me.}
    \exampleitem{৫. আমরা তাকে সাহায্য করতে পারতাম।}{5. We might have helped him.}
    \exampleitem{৬. রিনা ভালো ফলাফল করতে পারতো।}{6. Rina might have made a good result.}
    \exampleitem{৭. সে সত্য কথা বলতে পারতো।}{7. He might have spoken the truth.}
    \exampleitem{৮. আপনি এখানে আসতে পারতেন।}{8. You might have come here.}
    \exampleitem{৯. তারা টাকা ধার দিতে পারতো।}{9. They might have lent the money.}
    \exampleitem{১০. আমি চিঠিটি পাঠাতে পারতাম।}{10. I might have sent the letter.}
\end{examplebox}
% ==========================================
% RULE 50
% ==========================================
\ruleheader{50.}{আমি ইংরেজিতে কথা বলতে সাহস করি।}{I dare speak English.}

\begin{examplebox}
    \exampleitem{১. আমি সেখানে যেতে সাহস করি।}{1. I dare go there.}
    \exampleitem{২. সে সত্য কথা বলতে সাহস করে।}{2. He dares speak the truth.}
    \exampleitem{৩. তারা প্রতিবাদ করতে সাহস করে।}{3. They dare protest.}
    \exampleitem{৪. তুমি কাজটি করতে সাহস করো।}{4. You dare do the work.}
    \exampleitem{৫. আমরা নদীতে সাঁতার কাটতে সাহস করি।}{5. We dare swim in the river.}
    \exampleitem{৬. রিনা একা থাকতে সাহস করে।}{6. Rina dares stay alone.}
    \exampleitem{৭. সে প্রশ্নটি জিজ্ঞাসা করতে সাহস করে।}{7. He dares ask the question.}
    \exampleitem{৮. আপনি এটি ছুঁতে সাহস করেন।}{8. You dare touch it.}
    \exampleitem{৯. তারা ঝুঁকি নিতে সাহস করে।}{9. They dare take risks.}
    \exampleitem{১০. আমি চেষ্টা করতে সাহস করি।}{10. I dare try.}
\end{examplebox}

% ==========================================
% RULE 51
% ==========================================
\ruleheader{51.}{আমি ইংরেজিতে কথা বলতাম। (অতীতের অভ্যাস)}{I used to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি নদীতে সাঁতার কাটতাম।}{1. I used to swim in the river.}
    \exampleitem{২. সে ধূমপান করতো।}{2. He used to smoke.}
    \exampleitem{৩. তারা মাঠে খেলতো।}{3. They used to play in the field.}
    \exampleitem{৪. তুমি সকালে হাঁটতে।}{4. You used to walk in the morning.}
    \exampleitem{৫. আমরা একসঙ্গে গান গাইতাম।}{5. We used to sing together.}
    \exampleitem{৬. রিনা ছবি আঁকতো।}{6. Rina used to draw pictures.}
    \exampleitem{৭. সে অনেক মিথ্যা বলতো।}{7. He used to tell many lies.}
    \exampleitem{৮. আপনি এখানে আসতেন।}{8. You used to come here.}
    \exampleitem{৯. তারা கடிন পরিশ্রম করতো।}{9. They used to work hard.}
    \exampleitem{১০. আমি চা পান করতাম।}{10. I used to drink tea.}
\end{examplebox}

% ==========================================
% RULE 52
% ==========================================
\ruleheader{52.}{আমি ইংরেজিতে কথা বলতে অভ্যস্ত।}{I am used to speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি সকালে উঠতে অভ্যস্ত।}{1. I am used to waking up early.}
    \exampleitem{২. সে কঠোর পরিশ্রম করতে অভ্যস্ত।}{2. He is used to working hard.}
    \exampleitem{৩. তারা শব্দে ঘুমাতে অভ্যস্ত।}{3. They are used to sleeping in noise.}
    \exampleitem{৪. তুমি একা থাকতে অভ্যস্ত।}{4. You are used to staying alone.}
    \exampleitem{৫. আমরা হাঁটতে অভ্যস্ত।}{5. We are used to walking.}
    \exampleitem{৬. রিনা রান্না করতে অভ্যস্ত।}{6. Rina is used to cooking.}
    \exampleitem{৭. সে চা পান করতে অভ্যস্ত।}{7. He is used to drinking tea.}
    \exampleitem{৮. আপনি এই পরিবেশে অভ্যস্ত।}{8. You are used to this environment.}
    \exampleitem{৯. তারা মিথ্যা শুনতে অভ্যস্ত।}{9. They are used to hearing lies.}
    \exampleitem{১০. আমি রাত জাগতে অভ্যস্ত।}{10. I am used to staying up late.}
\end{examplebox}

% ==========================================
% RULE 53
% ==========================================
\ruleheader{53.}{আমাকে ইংরেজিতে কথা বলতে হয়/ বলার কথা আছে।}{I am to speak English.}

\begin{examplebox}
    \exampleitem{১. আমাকে সেখানে যেতে হয়।}{1. I am to go there.}
    \exampleitem{২. তাকে কাজটি করতে হয়।}{2. He is to do the work.}
    \exampleitem{৩. তাদের আজ আসার কথা আছে।}{3. They are to come today.}
    \exampleitem{৪. তোমাকে সকালে উঠতে হয়।}{4. You are to wake up early.}
    \exampleitem{৫. আমাদের মিটিংয়ে যোগ দেওয়ার কথা আছে।}{5. We are to attend the meeting.}
    \exampleitem{৬. রিনাকে রান্না করতে হয়।}{6. Rina is to cook.}
    \exampleitem{৭. তাকে বাজারে যাওয়ার কথা আছে।}{7. He is to go to the market.}
    \exampleitem{৮. আপনাকে অপেক্ষা করতে হয়।}{8. You are to wait.}
    \exampleitem{৯. তাদের টাকা দেওয়ার কথা আছে।}{9. They are to pay the money.}
    \exampleitem{১০. আমাকে এখন পড়তে হয়।}{10. I am to study now.}
\end{examplebox}

% ==========================================
% RULE 54
% ==========================================
\ruleheader{54.}{আমার ইংরেজিতে কথা বলা বলা ভাব।}{I am about to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার কাঁদো কাঁদো ভাব।}{1. I am about to cry.}
    \exampleitem{২. তার মড়ো মড়ো ভাব।}{2. He is about to die.}
    \exampleitem{৩. ট্রেনটি ছাড়ো ছাড়ো ভাব।}{3. The train is about to leave.}
    \exampleitem{৪. সূর্যটি ডোবো ডোবো ভাব।}{4. The sun is about to set.}
    \exampleitem{৫. আমাদের পৌঁছানো পৌঁছানো ভাব।}{5. We are about to reach.}
    \exampleitem{৬. রিনার ঘুমাই ঘুমাই ভাব।}{6. Rina is about to sleep.}
    \exampleitem{৭. বৃষ্টিটি নামো নামো ভাব।}{7. It is about to rain.}
    \exampleitem{৮. অনুষ্ঠানটি শুরু হওয়ার ভাব।}{8. The program is about to start.}
    \exampleitem{৯. তাদের যাওয়ার ভাব।}{9. They are about to leave.}
    \exampleitem{১০. আমার কাজটি শেষ হওয়ার ভাব।}{10. I am about to finish the work.}
\end{examplebox}

% ==========================================
% RULE 55
% ==========================================
\ruleheader{55.}{আমার ইংরেজিতে কথা বলা বাকী। / এখনো বলা হয়নি।}{I am yet to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার কাজটি করা বাকী।}{1. I am yet to do the work.}
    \exampleitem{২. তার এখানে আসা বাকী।}{2. He is yet to come here.}
    \exampleitem{৩. তাদের টাকা দেওয়া বাকী।}{3. They are yet to pay the money.}
    \exampleitem{৪. তোমার সিদ্ধান্ত নেওয়া বাকী।}{4. You are yet to take a decision.}
    \exampleitem{৫. আমাদের ঢাকা পৌঁছানো বাকী।}{5. We are yet to reach Dhaka.}
    \exampleitem{৬. রিনার রান্না করা বাকী।}{6. Rina is yet to cook.}
    \exampleitem{৭. তার বিয়ে করা বাকী।}{7. He is yet to marry.}
    \exampleitem{৮. আপনার খবরটি শোনা বাকী।}{8. You are yet to hear the news.}
    \exampleitem{৯. তাদের খাওয়া বাকী।}{9. They are yet to eat.}
    \exampleitem{১০. আমার বইটি পড়া বাকী।}{10. I am yet to read the book.}
\end{examplebox}

% ==========================================
% RULE 56
% ==========================================
\ruleheader{56.}{আমি ইংরেজিতে কথা বলতে সক্ষম।}{I am able to speak English. / I am capable of speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে সক্ষম।}{1. I am able to do the work.}
    \exampleitem{২. সে সিদ্ধান্ত নিতে সক্ষম।}{2. He is capable of making decisions.}
    \exampleitem{৩. তারা জিততে সক্ষম।}{3. They are able to win.}
    \exampleitem{৪. তুমি সমস্যাটি সমাধান করতে সক্ষম।}{4. You are capable of solving the problem.}
    \exampleitem{৫. আমরা সাহায্য করতে সক্ষম।}{5. We are able to help.}
    \exampleitem{৬. রিনা একা চলতে সক্ষম।}{6. Rina is capable of walking alone.}
    \exampleitem{৭. সে দ্রুত দৌড়াতে সক্ষম।}{7. He is able to run fast.}
    \exampleitem{৮. আপনি এটি পরিবর্তন করতে সক্ষম।}{8. You are capable of changing it.}
    \exampleitem{৯. তারা ঝুঁকি নিতে সক্ষম।}{9. They are able to take risks.}
    \exampleitem{১০. আমি দায়িত্ব নিতে সক্ষম।}{10. I am capable of taking responsibility.}
\end{examplebox}

% ==========================================
% RULE 57
% ==========================================
\ruleheader{57.}{আমি ইংরেজিতে কথা বলতে অক্ষম।}{I am unable to speak English. / I am incapable of speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে অক্ষম।}{1. I am unable to do the work.}
    \exampleitem{২. সে বুঝতে অক্ষম।}{2. He is incapable of understanding.}
    \exampleitem{৩. তারা হাঁটতে অক্ষম।}{3. They are unable to walk.}
    \exampleitem{৪. তুমি একা যেতে অক্ষম।}{4. You are incapable of going alone.}
    \exampleitem{৫. আমরা সাহায্য করতে অক্ষম।}{5. We are unable to help.}
    \exampleitem{৬. রিনা রান্না করতে অক্ষম।}{6. Rina is incapable of cooking.}
    \exampleitem{৭. সে দেখতে অক্ষম।}{7. He is unable to see.}
    \exampleitem{৮. আপনি শুনতে অক্ষম।}{8. You are incapable of hearing.}
    \exampleitem{৯. তারা ঋণ শোধ করতে অক্ষম।}{9. They are unable to pay the debt.}
    \exampleitem{১০. আমি উত্তর দিতে অক্ষম।}{10. I am incapable of answering.}
\end{examplebox}

% ==========================================
% RULE 58
% ==========================================
\ruleheader{58.}{আমার ইংরেজিতে কথা বলার কথা আছে।}{I am supposed to / expected to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার সেখানে যাওয়ার কথা আছে।}{1. I am supposed to go there.}
    \exampleitem{২. তার আজ আসার কথা আছে।}{2. He is expected to come today.}
    \exampleitem{৩. তাদের জেতার কথা আছে।}{3. They are supposed to win.}
    \exampleitem{৪. তোমার আমাকে জানানোর কথা আছে।}{4. You are expected to inform me.}
    \exampleitem{৫. আমাদের মিটিংয়ে থাকার কথা আছে।}{5. We are supposed to be in the meeting.}
    \exampleitem{৬. রিনার গান গাওয়ার কথা আছে।}{6. Rina is expected to sing a song.}
    \exampleitem{৭. বৃষ্টি হওয়ার কথা আছে।}{7. It is supposed to rain.}
    \exampleitem{৮. আপনার কাজ শুরু করার কথা আছে।}{8. You are expected to start working.}
    \exampleitem{৯. তাদের বাড়ি ফেরার কথা আছে।}{9. They are supposed to return home.}
    \exampleitem{১০. আমার তাকে সাহায্য করার কথা আছে।}{10. I am expected to help him.}
\end{examplebox}

% ==========================================
% RULE 59
% ==========================================
\ruleheader{59.}{আমি ইংরেজিতে কথা বলতে বাধ্য।}{I am compelled to / forced to / bound to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করতে বাধ্য।}{1. I am bound to do the work.}
    \exampleitem{২. সে চাকরি ছাড়তে বাধ্য।}{2. He is forced to leave the job.}
    \exampleitem{৩. তারা নিয়ম মানতে বাধ্য।}{3. They are compelled to follow the rules.}
    \exampleitem{৪. তুমি সত্য বলতে বাধ্য।}{4. You are bound to tell the truth.}
    \exampleitem{৫. আমরা ফিরে আসতে বাধ্য।}{5. We are forced to return.}
    \exampleitem{৬. রিনা একমত হতে বাধ্য।}{6. Rina is compelled to agree.}
    \exampleitem{৭. সে টাকা দিতে বাধ্য।}{7. He is bound to pay the money.}
    \exampleitem{৮. আপনি স্বীকার করতে বাধ্য।}{8. You are forced to confess.}
    \exampleitem{৯. তারা ক্ষমা চাইতে বাধ্য।}{9. They are compelled to apologize.}
    \exampleitem{১০. আমি সিদ্ধান্ত নিতে বাধ্য।}{10. I am bound to make a decision.}
\end{examplebox}

% ==========================================
% RULE 60
% ==========================================
\ruleheader{60.}{আমি ইংরেজিতে কথা বলতে যাচ্ছি।}{I am going to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি একটি গাড়ি কিনতে যাচ্ছি।}{1. I am going to buy a car.}
    \exampleitem{২. সে নতুন ব্যবসা শুরু করতে যাচ্ছে।}{2. He is going to start a new business.}
    \exampleitem{৩. তারা ঢাকা যেতে যাচ্ছে।}{3. They are going to go to Dhaka.}
    \exampleitem{৪. তুমি একটি চিঠি লিখতে যাচ্ছ।}{4. You are going to write a letter.}
    \exampleitem{৫. আমরা একটি বাড়ি তৈরি করতে যাচ্ছি।}{5. We are going to build a house.}
    \exampleitem{৬. রিনা রান্না করতে যাচ্ছে।}{6. Rina is going to cook.}
    \exampleitem{৭. বৃষ্টি হতে যাচ্ছে।}{7. It is going to rain.}
    \exampleitem{৮. আপনি পদত্যাগ করতে যাচ্ছেন।}{8. You are going to resign.}
    \exampleitem{৯. তারা একটি মিটিং করতে যাচ্ছে।}{9. They are going to hold a meeting.}
    \exampleitem{১০. আমি তোমাকে একটি গল্প বলতে যাচ্ছি।}{10. I am going to tell you a story.}
\end{examplebox}

% ==========================================
% RULE 61
% ==========================================
\ruleheader{61.}{আমার বরং ইংরেজিতে কথা বলা ভালো।}{I had better speak English.}

\begin{examplebox}
    \exampleitem{১. আমার বরং এখন যাওয়া ভালো।}{1. I had better go now.}
    \exampleitem{২. তার বরং ডাক্তারের কাছে যাওয়া ভালো।}{2. He had better go to a doctor.}
    \exampleitem{৩. তাদের বরং পড়ালেখা করা ভালো।}{3. They had better study.}
    \exampleitem{৪. তোমার বরং চুপ থাকা ভালো।}{4. You had better keep quiet.}
    \exampleitem{৫. আমাদের বরং অপেক্ষা করা ভালো।}{5. We had better wait.}
    \exampleitem{৬. রিনার বরং বিশ্রাম নেওয়া ভালো।}{6. Rina had better take a rest.}
    \exampleitem{৭. তার বরং সত্য কথা বলা ভালো।}{7. He had better speak the truth.}
    \exampleitem{৮. আপনার বরং কাজ শুরু করা ভালো।}{8. You had better start working.}
    \exampleitem{৯. তাদের বরং ক্ষমা চাওয়া ভালো।}{9. They had better apologize.}
    \exampleitem{১০. আমার বরং চেষ্টা করা ভালো।}{10. I had better try.}
\end{examplebox}

% ==========================================
% RULE 62
% ==========================================
\ruleheader{62.}{আমি বরং ইংরেজিতে কথা বলবো তবু ভয় করবো না।}{I would rather speak English than fear.}

\begin{examplebox}
    \exampleitem{১. আমি বরং মরবো তবু ভিক্ষা করবো না।}{1. I would rather die than beg.}
    \exampleitem{২. সে বরং ফেল করবে তবু নকল করবে না।}{2. He would rather fail than copy.}
    \exampleitem{৩. তারা বরং হারবে তবু প্রতারণা করবে না।}{3. They would rather lose than cheat.}
    \exampleitem{৪. তুমি বরং না খেয়ে থাকবে তবু চুরি করবে না।}{4. You would rather starve than steal.}
    \exampleitem{৫. আমরা বরং পায়ে হাঁটবো তবু বাসে উঠবো না।}{5. We would rather walk than take a bus.}
    \exampleitem{৬. রিনা বরং একা থাকবে তবু বিয়ে করবে না।}{6. Rina would rather stay alone than marry.}
    \exampleitem{৭. সে বরং চাকরি ছাড়বে তবু অপমান সইবে না।}{7. He would rather quit the job than bear insult.}
    \exampleitem{৮. আপনি বরং কষ্ট করবেন তবু সাহায্য চাইবেন না।}{8. You would rather suffer than ask for help.}
    \exampleitem{৯. তারা বরং মিথ্যা বলবে তবু ধরা পড়বে না।}{9. They would rather lie than get caught.}
    \exampleitem{১০. আমি বরং চা খাবো তবু কফি খাবো না।}{10. I would rather drink tea than coffee.}
\end{examplebox}

% ==========================================
% RULE 63
% ==========================================
\ruleheader{63.}{আমি ইংরেজিতে কথা বলতে ইচ্ছুক।}{I am willing to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমাকে সাহায্য করতে ইচ্ছুক।}{1. I am willing to help you.}
    \exampleitem{২. সে সেখানে যেতে ইচ্ছুক।}{2. He is willing to go there.}
    \exampleitem{৩. তারা কাজটি করতে ইচ্ছুক।}{3. They are willing to do the work.}
    \exampleitem{৪. তুমি শিখতে ইচ্ছুক।}{4. You are willing to learn.}
    \exampleitem{৫. আমরা বিনিয়োগ করতে ইচ্ছুক।}{5. We are willing to invest.}
    \exampleitem{৬. রিনা কাজটিতে যোগ দিতে ইচ্ছুক।}{6. Rina is willing to join the work.}
    \exampleitem{৭. সে অপেক্ষা করতে ইচ্ছুক।}{7. He is willing to wait.}
    \exampleitem{৮. আপনি টাকা দিতে ইচ্ছুক।}{8. You are willing to pay the money.}
    \exampleitem{৯. তারা আলোচনা করতে ইচ্ছুক।}{9. They are willing to discuss.}
    \exampleitem{১০. আমি দায়িত্ব নিতে ইচ্ছুক।}{10. I am willing to take responsibility.}
\end{examplebox}

% ==========================================
% RULE 64
% ==========================================
\ruleheader{64.}{আমি ইংরেজিতে কথা বলতে অনিচ্ছুক।}{I am unwilling to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটিতে যোগ দিতে অনিচ্ছুক।}{1. I am unwilling to join the work.}
    \exampleitem{২. সে সত্য বলতে অনিচ্ছুক।}{2. He is unwilling to tell the truth.}
    \exampleitem{৩. তারা নিয়ম মানতে অনিচ্ছুক।}{3. They are unwilling to follow the rules.}
    \exampleitem{৪. তুমি আপোষ করতে অনিচ্ছুক।}{4. You are unwilling to compromise.}
    \exampleitem{৫. আমরা টাকা দিতে অনিচ্ছুক।}{5. We are unwilling to pay the money.}
    \exampleitem{৬. রিনা সেখানে যেতে অনিচ্ছুক।}{6. Rina is unwilling to go there.}
    \exampleitem{৭. সে দায়িত্ব নিতে অনিচ্ছুক।}{7. He is unwilling to take responsibility.}
    \exampleitem{৮. আপনি ক্ষমা করতে অনিচ্ছুক।}{8. You are unwilling to forgive.}
    \exampleitem{৯. তারা কথা শুনতে অনিচ্ছুক।}{9. They are unwilling to listen.}
    \exampleitem{১০. আমি তাকে সাহায্য করতে অনিচ্ছুক।}{10. I am unwilling to help him.}
\end{examplebox}

% ==========================================
% RULE 65
% ==========================================
\ruleheader{65.}{আমার ইংরেজিতে কথা বলার সম্ভাবনা আছে।}{I am likely to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার চাকরিটি পাওয়ার সম্ভাবনা আছে।}{1. I am likely to get the job.}
    \exampleitem{২. তার আজ আসার সম্ভাবনা আছে।}{2. He is likely to come today.}
    \exampleitem{৩. তাদের জেতার সম্ভাবনা আছে।}{3. They are likely to win.}
    \exampleitem{৪. আজ বৃষ্টি হওয়ার সম্ভাবনা আছে।}{4. It is likely to rain today.}
    \exampleitem{৫. আমাদের ঢাকা যাওয়ার সম্ভাবনা আছে।}{5. We are likely to go to Dhaka.}
    \exampleitem{৬. রিনার পাস করার সম্ভাবনা আছে।}{6. Rina is likely to pass.}
    \exampleitem{৭. তার বিয়ে করার সম্ভাবনা আছে।}{7. He is likely to marry.}
    \exampleitem{৮. আপনার প্রমোশন পাওয়ার সম্ভাবনা আছে।}{8. You are likely to get a promotion.}
    \exampleitem{৯. তাদের বাড়ি বিক্রি করার সম্ভাবনা আছে।}{9. They are likely to sell the house.}
    \exampleitem{১০. আমার সেখানে উপস্থিত থাকার সম্ভাবনা আছে।}{10. I am likely to be present there.}
\end{examplebox}

% ==========================================
% RULE 66
% ==========================================
\ruleheader{66.}{আমার ইংরেজিতে কথা বলার সম্ভাবনা নেই।}{I am unlikely to speak English.}

\begin{examplebox}
    \exampleitem{১. আমার চাকরিটি পাওয়ার সম্ভাবনা নেই।}{1. I am unlikely to get the job.}
    \exampleitem{২. তার আজ আসার সম্ভাবনা নেই।}{2. He is unlikely to come today.}
    \exampleitem{৩. তাদের জেতার সম্ভাবনা নেই।}{3. They are unlikely to win.}
    \exampleitem{৪. আজ বৃষ্টি হওয়ার সম্ভাবনা নেই।}{4. It is unlikely to rain today.}
    \exampleitem{৫. আমাদের ঢাকা যাওয়ার সম্ভাবনা নেই।}{5. We are unlikely to go to Dhaka.}
    \exampleitem{৬. রিনার পাস করার সম্ভাবনা নেই।}{6. Rina is unlikely to pass.}
    \exampleitem{৭. তার ভুল করার সম্ভাবনা নেই।}{7. He is unlikely to make a mistake.}
    \exampleitem{৮. আপনার সেখানে যাওয়ার সম্ভাবনা নেই।}{8. You are unlikely to go there.}
    \exampleitem{৯. তাদের রাজি হওয়ার সম্ভাবনা নেই।}{9. They are unlikely to agree.}
    \exampleitem{১০. আমার তাকে সাহায্য করার সম্ভাবনা নেই।}{10. I am unlikely to help him.}
\end{examplebox}

% ==========================================
% RULE 67
% ==========================================
\ruleheader{67.}{আমি ইংরেজিতে কথা বলতে আগ্রহী।}{I am interested to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি বিষয়টি শিখতে আগ্রহী।}{1. I am interested to learn the subject.}
    \exampleitem{২. সে বইটি পড়তে আগ্রহী।}{2. He is interested to read the book.}
    \exampleitem{৩. তারা নতুন ব্যবসা শুরু করতে আগ্রহী।}{3. They are interested to start a new business.}
    \exampleitem{৪. তুমি বিদেশ যেতে আগ্রহী।}{4. You are interested to go abroad.}
    \exampleitem{৫. আমরা কাজটিতে যোগ দিতে আগ্রহী।}{5. We are interested to join the work.}
    \exampleitem{৬. রিনা গান শিখতে আগ্রহী।}{6. Rina is interested to learn singing.}
    \exampleitem{৭. সে বাড়িটি কিনতে আগ্রহী।}{7. He is interested to buy the house.}
    \exampleitem{৮. আপনি বিনিয়োগ করতে আগ্রহী।}{8. You are interested to invest.}
    \exampleitem{৯. তারা আলোচনা করতে আগ্রহী।}{9. They are interested to discuss.}
    \exampleitem{১০. আমি গল্পটি শুনতে আগ্রহী।}{10. I am interested to hear the story.}
\end{examplebox}

% ==========================================
% RULE 68
% ==========================================
\ruleheader{68.}{আমি ইংরেজিতে কথা বলতে অনাগ্রহী।}{I am uninterested to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি বিষয়টি শিখতে অনাগ্রহী।}{1. I am uninterested to learn the subject.}
    \exampleitem{২. সে বইটি পড়তে অনাগ্রহী।}{2. He is uninterested to read the book.}
    \exampleitem{৩. তারা নতুন ব্যবসা শুরু করতে অনাগ্রহী।}{3. They are uninterested to start a new business.}
    \exampleitem{৪. তুমি সেখানে যেতে অনাগ্রহী।}{4. You are uninterested to go there.}
    \exampleitem{৫. আমরা কাজটিতে যোগ দিতে অনাগ্রহী।}{5. We are uninterested to join the work.}
    \exampleitem{৬. রিনা গান শিখতে অনাগ্রহী।}{6. Rina is uninterested to learn singing.}
    \exampleitem{৭. সে সাহায্য করতে অনাগ্রহী।}{7. He is uninterested to help.}
    \exampleitem{৮. আপনি কথা বলতে অনাগ্রহী।}{8. You are uninterested to talk.}
    \exampleitem{৯. তারা শুনতে অনাগ্রহী।}{9. They are uninterested to listen.}
    \exampleitem{১০. আমি রাজনীতি নিয়ে ভাবতে অনাগ্রহী।}{10. I am uninterested to think about politics.}
\end{examplebox}

% ==========================================
% RULE 69
% ==========================================
\ruleheader{69.}{আমি ইংরেজিতে কথা বলতে দৃঢ় প্রতিজ্ঞ।}{I am determined to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি সফল হতে দৃঢ় প্রতিজ্ঞ।}{1. I am determined to succeed.}
    \exampleitem{২. সে লক্ষ্য অর্জন করতে দৃঢ় প্রতিজ্ঞ।}{2. He is determined to achieve his goal.}
    \exampleitem{৩. তারা জিততে দৃঢ় প্রতিজ্ঞ।}{3. They are determined to win.}
    \exampleitem{৪. তুমি ইংরেজি শিখতে দৃঢ় প্রতিজ্ঞ।}{4. You are determined to learn English.}
    \exampleitem{৫. আমরা কাজটি শেষ করতে দৃঢ় প্রতিজ্ঞ।}{5. We are determined to finish the work.}
    \exampleitem{৬. রিনা ডাক্তার হতে দৃঢ় প্রতিজ্ঞ।}{6. Rina is determined to be a doctor.}
    \exampleitem{৭. সে সত্য প্রকাশ করতে দৃঢ় প্রতিজ্ঞ।}{7. He is determined to reveal the truth.}
    \exampleitem{৮. আপনি পরিবর্তন আনতে দৃঢ় প্রতিজ্ঞ।}{8. You are determined to bring a change.}
    \exampleitem{৯. তারা সমস্যাটি সমাধান করতে দৃঢ় প্রতিজ্ঞ।}{9. They are determined to solve the problem.}
    \exampleitem{১০. আমি আমার স্বপ্ন পূরণ করতে দৃঢ় প্রতিজ্ঞ।}{10. I am determined to fulfill my dream.}
\end{examplebox}
% ==========================================
% RULE 70
% ==========================================
\ruleheader{70.}{আমি ইংরেজিতে কথা বলার বিষয়ে অতি উৎসাহী।}{I am enthusiastic about speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করার বিষয়ে অতি উৎসাহী।}{1. I am enthusiastic about doing the work.}
    \exampleitem{২. সে সেখানে যাওয়ার বিষয়ে অতি উৎসাহী।}{2. He is enthusiastic about going there.}
    \exampleitem{৩. তারা খেলায় অংশগ্রহণের বিষয়ে অতি উৎসাহী।}{3. They are enthusiastic about participating in the game.}
    \exampleitem{৪. তুমি নতুন ভাষা শেখার বিষয়ে অতি উৎসাহী।}{4. You are enthusiastic about learning a new language.}
    \exampleitem{৫. আমরা প্রকল্পটি শুরু করার বিষয়ে অতি উৎসাহী।}{5. We are enthusiastic about starting the project.}
    \exampleitem{৬. রিনা গান গাওয়ার বিষয়ে অতি উৎসাহী।}{6. Rina is enthusiastic about singing a song.}
    \exampleitem{৭. সে ভ্রমণ করার বিষয়ে অতি উৎসাহী।}{7. He is enthusiastic about traveling.}
    \exampleitem{৮. আপনি সাহায্য করার বিষয়ে অতি উৎসাহী।}{8. You are enthusiastic about helping.}
    \exampleitem{৯. তারা নতুন কিছু জানার বিষয়ে অতি উৎসাহী।}{9. They are enthusiastic about knowing something new.}
    \exampleitem{১০. আমি বইটি পড়ার বিষয়ে অতি উৎসাহী।}{10. I am enthusiastic about reading the book.}
\end{examplebox}

% ==========================================
% RULE 71
% ==========================================
\ruleheader{71.}{আমি ইংরেজিতে কথা বলার বিষয়ে নিরুৎসাহিত।}{I am unenthusiastic about speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি করার বিষয়ে নিরুৎসাহিত।}{1. I am unenthusiastic about doing the work.}
    \exampleitem{২. সে সেখানে যাওয়ার বিষয়ে নিরুৎসাহিত।}{2. He is unenthusiastic about going there.}
    \exampleitem{৩. তারা খেলায় অংশগ্রহণের বিষয়ে নিরুৎসাহিত।}{3. They are unenthusiastic about participating in the game.}
    \exampleitem{৪. তুমি নতুন ভাষা শেখার বিষয়ে নিরুৎসাহিত।}{4. You are unenthusiastic about learning a new language.}
    \exampleitem{৫. আমরা প্রকল্পটি শুরু করার বিষয়ে নিরুৎসাহিত।}{5. We are unenthusiastic about starting the project.}
    \exampleitem{৬. রিনা গান গাওয়ার বিষয়ে নিরুৎসাহিত।}{6. Rina is unenthusiastic about singing a song.}
    \exampleitem{৭. সে ভ্রমণ করার বিষয়ে নিরুৎসাহিত।}{7. He is unenthusiastic about traveling.}
    \exampleitem{৮. আপনি সাহায্য করার বিষয়ে নিরুৎসাহিত।}{8. You are unenthusiastic about helping.}
    \exampleitem{৯. তারা নতুন কিছু জানার বিষয়ে নিরুৎসাহিত।}{9. They are unenthusiastic about knowing something new.}
    \exampleitem{১০. আমি বইটি পড়ার বিষয়ে নিরুৎসাহিত।}{10. I am unenthusiastic about reading the book.}
\end{examplebox}

% ==========================================
% RULE 72
% ==========================================
\ruleheader{72.}{আমি ইংরেজিতে কথা বলে দুঃখিত।}{I am sorry to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি দেরি করে আসার জন্য দুঃখিত।}{1. I am sorry to come late.}
    \exampleitem{২. সে তোমাকে বিরক্ত করার জন্য দুঃখিত।}{2. He is sorry to disturb you.}
    \exampleitem{৩. তারা খবরটি শুনে দুঃখিত।}{3. They are sorry to hear the news.}
    \exampleitem{৪. তুমি ভুলটি করার জন্য দুঃখিত।}{4. You are sorry to make the mistake.}
    \exampleitem{৫. আমরা তোমাকে আঘাত করার জন্য দুঃখিত।}{5. We are sorry to hurt you.}
    \exampleitem{৬. রিনা সুযোগটি হারানোর জন্য দুঃখিত।}{6. Rina is sorry to lose the opportunity.}
    \exampleitem{৭. সে এটি বলার জন্য দুঃখিত।}{7. He is sorry to say this.}
    \exampleitem{৮. আপনি সত্যটি জানার জন্য দুঃখিত।}{8. You are sorry to know the truth.}
    \exampleitem{৯. তারা উপস্থিত না থাকার জন্য দুঃখিত।}{9. They are sorry to be absent.}
    \exampleitem{১০. আমি তোমাকে হতাশ করার জন্য দুঃখিত।}{10. I am sorry to disappoint you.}
\end{examplebox}

% ==========================================
% RULE 73
% ==========================================
\ruleheader{73.}{আমি ইংরেজিতে কথা বলে খুশি / আনন্দিত।}{I am glad to / happy to / pleased to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমাকে সাহায্য করতে পেরে খুশি।}{1. I am glad to help you.}
    \exampleitem{২. সে খবরটি শুনে আনন্দিত।}{2. He is happy to hear the news.}
    \exampleitem{৩. তারা তোমার সাথে দেখা করে আনন্দিত।}{3. They are pleased to meet you.}
    \exampleitem{৪. তুমি পাস করতে পেরে খুশি।}{4. You are happy to pass.}
    \exampleitem{৫. আমরা তোমাকে এখানে পেয়ে আনন্দিত।}{5. We are glad to have you here.}
    \exampleitem{৬. রিনা পুরস্কারটি পেয়ে খুশি।}{6. Rina is happy to receive the prize.}
    \exampleitem{৭. সে কাজটি শেষ করতে পেরে আনন্দিত।}{7. He is pleased to finish the work.}
    \exampleitem{৮. আপনি সত্যটি জানতে পেরে খুশি।}{8. You are glad to know the truth.}
    \exampleitem{৯. তারা অনুষ্ঠানে যোগ দিতে পেরে আনন্দিত।}{9. They are happy to join the program.}
    \exampleitem{১০. আমি তোমাকে আবার দেখতে পেরে আনন্দিত।}{10. I am pleased to see you again.}
\end{examplebox}

% ==========================================
% RULE 74
% ==========================================
\ruleheader{74.}{আমি ইংরেজিতে কথা বলে খুব খুশি / আনন্দিত।}{I am delighted to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি খবরটি শুনে খুব খুশি।}{1. I am delighted to hear the news.}
    \exampleitem{২. সে উপহারটি পেয়ে খুব আনন্দিত।}{2. He is delighted to receive the gift.}
    \exampleitem{৩. তারা তোমাকে সাহায্য করতে পেরে খুব খুশি।}{3. They are delighted to help you.}
    \exampleitem{৪. তুমি পাস করতে পেরে খুব আনন্দিত।}{4. You are delighted to pass.}
    \exampleitem{৫. আমরা তাকে এখানে দেখে খুব খুশি।}{5. We are delighted to see him here.}
    \exampleitem{৬. রিনা চাকরিটি পেয়ে খুব আনন্দিত।}{6. Rina is delighted to get the job.}
    \exampleitem{৭. সে সুযোগটি পেয়ে খুব খুশি।}{7. He is delighted to get the opportunity.}
    \exampleitem{৮. আপনি সত্যটি জানতে পেরে খুব আনন্দিত।}{8. You are delighted to know the truth.}
    \exampleitem{৯. তারা ম্যাচটি জিততে পেরে খুব খুশি।}{9. They are delighted to win the match.}
    \exampleitem{১০. আমি তোমার সাফল্য দেখে খুব আনন্দিত।}{10. I am delighted to see your success.}
\end{examplebox}

% ==========================================
% RULE 75
% ==========================================
\ruleheader{75.}{আমি ইংরেজিতে কথা বলে মর্মাহত।}{I am shocked to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি খবরটি শুনে মর্মাহত।}{1. I am shocked to hear the news.}
    \exampleitem{২. সে তার আচরণ দেখে মর্মাহত।}{2. He is shocked to see his behavior.}
    \exampleitem{৩. তারা ঘটনাটি জেনে মর্মাহত।}{3. They are shocked to know the incident.}
    \exampleitem{৪. তুমি ফলাফলটি দেখে মর্মাহত।}{4. You are shocked to see the result.}
    \exampleitem{৫. আমরা তার মৃত্যুতে মর্মাহত।}{5. We are shocked at his death.} % Modified slightly for natural flow
    \exampleitem{৬. রিনা সত্যটি আবিষ্কার করে মর্মাহত।}{6. Rina is shocked to discover the truth.}
    \exampleitem{৭. সে পরিস্থিতিটি দেখে মর্মাহত।}{7. He is shocked to see the situation.}
    \exampleitem{৮. আপনি সিদ্ধান্তটি শুনে মর্মাহত।}{8. You are shocked to hear the decision.}
    \exampleitem{৯. তারা এমন কথা শুনে মর্মাহত।}{9. They are shocked to hear such words.}
    \exampleitem{১০. আমি এই ক্ষতিতে মর্মাহত।}{10. I am shocked at this loss.} % Modified slightly for natural flow
\end{examplebox}

% ==========================================
% RULE 76
% ==========================================
\ruleheader{76.}{আমি ইংরেজিতে কথা বলে বিস্মিত / অবাক।}{I am surprised to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমাকে এখানে দেখে অবাক।}{1. I am surprised to see you here.}
    \exampleitem{২. সে ফলাফলটি জেনে বিস্মিত।}{2. He is surprised to know the result.}
    \exampleitem{৩. তারা খবরটি শুনে অবাক।}{3. They are surprised to hear the news.}
    \exampleitem{৪. তুমি তার সিদ্ধান্ত দেখে বিস্মিত।}{4. You are surprised to see his decision.}
    \exampleitem{৫. আমরা উপহারটি পেয়ে অবাক।}{5. We are surprised to receive the gift.}
    \exampleitem{৬. রিনা তাকে কল করতে দেখে বিস্মিত।}{6. Rina is surprised to see him calling.}
    \exampleitem{৭. সে দ্রুত পরিবর্তন দেখে অবাক।}{7. He is surprised to see the rapid change.}
    \exampleitem{৮. আপনি সত্যটি আবিষ্কার করে বিস্মিত।}{8. You are surprised to discover the truth.}
    \exampleitem{৯. তারা তাকে জিততে দেখে অবাক।}{9. They are surprised to see him win.}
    \exampleitem{১০. আমি তার সাহসিকতা দেখে বিস্মিত।}{10. I am surprised to see his bravery.}
\end{examplebox}

% ==========================================
% RULE 77
% ==========================================
\ruleheader{77.}{আমি ইংরেজিতে কথা বলতে ভীষণ / প্রচন্ডরকম আগ্রহী।}{I am eager to / keen to / excited to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি বিষয়টি জানতে ভীষণ আগ্রহী।}{1. I am eager to know the matter.}
    \exampleitem{২. সে বইটি পড়তে প্রচন্ডরকম আগ্রহী।}{2. He is keen to read the book.}
    \exampleitem{৩. তারা সেখানে যেতে ভীষণ আগ্রহী।}{3. They are excited to go there.}
    \exampleitem{৪. তুমি তাকে সাহায্য করতে প্রচন্ডরকম আগ্রহী।}{4. You are keen to help him.}
    \exampleitem{৫. আমরা প্রকল্পটি শুরু করতে ভীষণ আগ্রহী।}{5. We are eager to start the project.}
    \exampleitem{৬. রিনা বিদেশ যেতে প্রচন্ডরকম আগ্রহী।}{6. Rina is excited to go abroad.}
    \exampleitem{৭. সে নতুন কাজ শিখতে ভীষণ আগ্রহী।}{7. He is keen to learn new work.}
    \exampleitem{৮. আপনি ম্যাচটি দেখতে প্রচন্ডরকম আগ্রহী।}{8. You are eager to watch the match.}
    \exampleitem{৯. তারা খবরটি শুনতে ভীষণ আগ্রহী।}{9. They are excited to hear the news.}
    \exampleitem{১০. আমি তার সাথে দেখা করতে প্রচন্ডরকম আগ্রহী।}{10. I am keen to meet him.}
\end{examplebox}

% ==========================================
% RULE 78
% ==========================================
\ruleheader{78.}{আমি ইংরেজিতে কথা বলতে আশাবাদী।}{I am hopeful of / optimistic about speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি জেতার ব্যাপারে আশাবাদী।}{1. I am optimistic about winning.}
    \exampleitem{২. সে ভালো ফলাফলের ব্যাপারে আশাবাদী।}{2. He is hopeful of a good result.}
    \exampleitem{৩. তারা চাকরিটি পাওয়ার বিষয়ে আশাবাদী।}{3. They are optimistic about getting the job.}
    \exampleitem{৪. তুমি সমস্যাটি সমাধানের ব্যাপারে আশাবাদী।}{4. You are hopeful of solving the problem.}
    \exampleitem{৫. আমরা প্রকল্পটি সফল হওয়ার বিষয়ে আশাবাদী।}{5. We are optimistic about the success of the project.}
    \exampleitem{৬. রিনা ঢাকা যাওয়ার ব্যাপারে আশাবাদী।}{6. Rina is hopeful of going to Dhaka.}
    \exampleitem{৭. সে একটি ভালো ভবিষ্যতের বিষয়ে আশাবাদী।}{7. He is optimistic about a good future.}
    \exampleitem{৮. আপনি সাহায্য পাওয়ার ব্যাপারে আশাবাদী।}{8. You are hopeful of getting help.}
    \exampleitem{৯. তারা ম্যাচটি জেতার বিষয়ে আশাবাদী।}{9. They are optimistic about winning the match.}
    \exampleitem{১০. আমি পরিবর্তনের ব্যাপারে আশাবাদী।}{10. I am hopeful of a change.}
\end{examplebox}

% ==========================================
% RULE 79
% ==========================================
\ruleheader{79.}{আমার ইংরেজিতে কথা বলতে ইচ্ছা করছে/ মন চাচ্ছে।}{I feel like speaking English.}

\begin{examplebox}
    \exampleitem{১. আমার চা খেতে ইচ্ছা করছে।}{1. I feel like drinking tea.}
    \exampleitem{২. তার এখন ঘুমাতে মন চাচ্ছে।}{2. He feels like sleeping now.}
    \exampleitem{৩. তাদের বৃষ্টিতে ভিজতে ইচ্ছা করছে।}{3. They feel like getting wet in the rain.}
    \exampleitem{৪. তোমার বাইরে যেতে মন চাচ্ছে।}{4. You feel like going outside.}
    \exampleitem{৫. আমাদের একটি গান গাইতে ইচ্ছা করছে।}{5. We feel like singing a song.}
    \exampleitem{৬. রিনার সিনেমা দেখতে মন চাচ্ছে।}{6. Rina feels like watching a movie.}
    \exampleitem{৭. তার একা থাকতে ইচ্ছা করছে।}{7. He feels like staying alone.}
    \exampleitem{৮. আপনার হাঁটতে মন চাচ্ছে।}{8. You feel like walking.}
    \exampleitem{৯. তাদের গল্প করতে ইচ্ছা করছে।}{9. They feel like gossiping.}
    \exampleitem{১০. আমার কিছু খেতে মন চাচ্ছে।}{10. I feel like eating something.}
\end{examplebox}

% ==========================================
% RULE 80
% ==========================================
\ruleheader{80.}{আমি ইংরেজিতে কথা বলতে প্রস্তুত।}{I am set to / prepared to / ready to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি কাজটি শুরু করতে প্রস্তুত।}{1. I am ready to start the work.}
    \exampleitem{২. সে পরীক্ষায় বসতে প্রস্তুত।}{2. He is prepared to sit for the exam.}
    \exampleitem{৩. তারা চ্যালেঞ্জটি নিতে প্রস্তুত।}{3. They are set to take the challenge.}
    \exampleitem{৪. তুমি সত্যটি শুনতে প্রস্তুত।}{4. You are ready to hear the truth.}
    \exampleitem{৫. আমরা তাকে সাহায্য করতে প্রস্তুত।}{5. We are prepared to help him.}
    \exampleitem{৬. রিনা বিদেশ যেতে প্রস্তুত।}{6. Rina is set to go abroad.}
    \exampleitem{৭. সে দায়িত্বটি নিতে প্রস্তুত।}{7. He is ready to take the responsibility.}
    \exampleitem{৮. আপনি প্রশ্ন করতে প্রস্তুত।}{8. You are prepared to ask questions.}
    \exampleitem{৯. তারা আলোচনা করতে প্রস্তুত।}{9. They are set to discuss.}
    \exampleitem{১০. আমি সেখানে যেতে প্রস্তুত।}{10. I am ready to go there.}
\end{examplebox}

% ==========================================
% RULE 81
% ==========================================
\ruleheader{81.}{আমি ইংরেজিতে কথা বলতে ভীত / সন্ত্রস্ত / আতঙ্কিত।}{I am afraid to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি একা যেতে ভয় পাই।}{1. I am afraid to go alone.}
    \exampleitem{২. সে কুকুর দেখে আতঙ্কিত।}{2. He is scared of dogs.}
    \exampleitem{৩. তারা অন্ধকারে থাকতে ভীত।}{3. They are terrified to stay in the dark.}
    \exampleitem{৪. তুমি সত্যটি বলতে ভয় পাচ্ছো।}{4. You are afraid of telling the truth.}
    \exampleitem{৫. আমরা কাজটি করতে সন্ত্রস্ত।}{5. We are frightened to do the work.}
    \exampleitem{৬. রিনা ভূত দেখে আতঙ্কিত।}{6. Rina is terrified of ghosts.}
    \exampleitem{৭. সে সাঁতার কাটতে ভয় পায়।}{7. He is scared to swim.}
    \exampleitem{৮. আপনি ঝুঁকি নিতে ভীত।}{8. You are afraid to take risks.}
    \exampleitem{৯. তারা সেখানে যেতে সন্ত্রস্ত।}{9. They are frightened of going there.}
    \exampleitem{১০. আমি তাকে বিরক্ত করতে ভয় পাই।}{10. I am afraid of disturbing him.}
\end{examplebox}

% ==========================================
% RULE 82
% ==========================================
\ruleheader{82.}{আমি ইংরেজিতে কথা বলতে অনিচ্ছুক / নারাজ / অনীহ / বিমুখ।}{I am reluctant to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি সেখানে যেতে অনিচ্ছুক।}{1. I am reluctant to go there.}
    \exampleitem{২. সে কাজটি করতে নারাজ।}{2. He is disinclined to do the work.}
    \exampleitem{৩. তারা টাকা দিতে অনীহ।}{3. They are unwilling to pay the money.}
    \exampleitem{৪. তুমি সত্যটি স্বীকার করতে 비মুখ।}{4. You are averse to admitting the truth.}
    \exampleitem{৫. আমরা সাহায্য করতে অনিচ্ছুক।}{5. We are indisposed to help.}
    \exampleitem{৬. রিনা তার সাথে কথা বলতে নারাজ।}{6. Rina is reluctant to talk to him.}
    \exampleitem{৭. সে পরিবর্তন মানতে অনীহ।}{7. He is unwilling to accept the change.}
    \exampleitem{৮. আপনি নতুন কিছু শুরু করতে 비মুখ।}{8. You are averse to starting something new.}
    \exampleitem{৯. তারা ঝুঁকি নিতে অনিচ্ছুক।}{9. They are disinclined to take risks.}
    \exampleitem{১০. আমি এটি বিশ্বাস করতে নারাজ।}{10. I am reluctant to believe this.}
\end{examplebox}

% ==========================================
% RULE 83
% ==========================================
\ruleheader{83.}{আমি ইংরেজিতে কথা বলতে (সানন্দে) প্রত্যাশা করি / প্রতীক্ষা করি।}{I look forward to speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমার সাথে দেখা করার প্রতীক্ষা করছি।}{1. I look forward to meeting you.}
    \exampleitem{২. সে খবরটি শোনার প্রত্যাশা করছে।}{2. He looks forward to hearing the news.}
    \exampleitem{৩. তারা অনুষ্ঠানে যোগ দেওয়ার প্রতীক্ষা করছে।}{3. They look forward to joining the program.}
    \exampleitem{৪. তুমি চিঠিটি পাওয়ার প্রত্যাশা করছো।}{4. You look forward to receiving the letter.}
    \exampleitem{৫. আমরা ছুটি কাটানোর প্রতীক্ষা করছি।}{5. We look forward to spending the vacation.}
    \exampleitem{৬. রিনা সেখানে যাওয়ার প্রত্যাশা করছে।}{6. Rina looks forward to going there.}
    \exampleitem{৭. সে কাজ শুরু করার প্রতীক্ষা করছে।}{7. He looks forward to starting the work.}
    \exampleitem{৮. আপনি তার উত্তর পাওয়ার প্রত্যাশা করছেন।}{8. You look forward to getting his reply.}
    \exampleitem{৯. তারা সাহায্য পাওয়ার প্রতীক্ষা করছে।}{9. They look forward to receiving help.}
    \exampleitem{১০. আমি তোমার সাথে কাজ করার প্রত্যাশা করছি।}{10. I look forward to working with you.}
\end{examplebox}

% ==========================================
% RULE 84
% ==========================================
\ruleheader{84.}{আমি ইংরেজিতে কথা বলতে নিশ্চিত।}{I am sure of / about speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি জেতার ব্যাপারে নিশ্চিত।}{1. I am sure of winning.}
    \exampleitem{২. সে কাজটি শেষ করার বিষয়ে নিশ্চিত।}{2. He is sure about finishing the work.}
    \exampleitem{৩. তারা সেখানে যাওয়ার ব্যাপারে নিশ্চিত।}{3. They are sure of going there.}
    \exampleitem{৪. তুমি পাস করার বিষয়ে নিশ্চিত।}{4. You are sure about passing.}
    \exampleitem{৫. আমরা সাহায্য পাওয়ার ব্যাপারে নিশ্চিত।}{5. We are sure of getting help.}
    \exampleitem{৬. রিনা খবরটি শোনার বিষয়ে নিশ্চিত।}{6. Rina is sure about hearing the news.}
    \exampleitem{৭. সে তাকে দেখার ব্যাপারে নিশ্চিত।}{7. He is sure of seeing him.}
    \exampleitem{৮. আপনি তাকে হারানোর বিষয়ে নিশ্চিত।}{8. You are sure about defeating him.}
    \exampleitem{৯. তারা টাকা পাওয়ার ব্যাপারে নিশ্চিত।}{9. They are sure of getting the money.}
    \exampleitem{১০. আমি তার ফিরে আসার বিষয়ে নিশ্চিত।}{10. I am sure about his returning.}
\end{examplebox}

% ==========================================
% RULE 85
% ==========================================
\ruleheader{85.}{আমি ইংরেজিতে কথা বলতে ভালোবাসি।}{I am fond of speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি বই পড়তে ভালোবাসি।}{1. I am fond of reading books.}
    \exampleitem{২. সে গান শুনতে ভালোবাসে।}{2. He is fond of listening to music.}
    \exampleitem{৩. তারা ফুটবল খেলতে ভালোবাসে।}{3. They are fond of playing football.}
    \exampleitem{৪. তুমি চা খেতে ভালোবাসো।}{4. You are fond of drinking tea.}
    \exampleitem{৫. আমরা ভ্রমণ করতে ভালোবাসি।}{5. We are fond of traveling.}
    \exampleitem{৬. রিনা ছবি আঁকতে ভালোবাসে।}{6. Rina is fond of drawing pictures.}
    \exampleitem{৭. সে বাগান করতে ভালোবাসে।}{7. He is fond of gardening.}
    \exampleitem{৮. আপনি রান্না করতে ভালোবাসেন।}{8. You are fond of cooking.}
    \exampleitem{৯. তারা মাছ ধরতে ভালোবাসে।}{9. They are fond of fishing.}
    \exampleitem{১০. আমি মিষ্টি খেতে ভালোবাসি।}{10. I am fond of eating sweets.}
\end{examplebox}

% ==========================================
% RULE 86
% ==========================================
\ruleheader{86.}{আমি ইংরেজিতে কথা বলতে মুক্ত / স্বাধীন।}{I am free to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি যেকোনো প্রশ্ন করতে স্বাধীন।}{1. I am free to ask any question.}
    \exampleitem{২. সে যেখানে খুশি যেতে মুক্ত।}{2. He is free to go anywhere.}
    \exampleitem{৩. তারা তাদের মতামত জানাতে স্বাধীন।}{3. They are free to express their opinion.}
    \exampleitem{৪. তুমি যা চাও করতে মুক্ত।}{4. You are free to do whatever you want.}
    \exampleitem{৫. আমরা কাজটিতে যোগ দিতে স্বাধীন।}{5. We are free to join the work.}
    \exampleitem{৬. রিনা তার সিদ্ধান্ত নিতে মুক্ত।}{6. Rina is free to make her decision.}
    \exampleitem{৭. সে এটি ব্যবহার করতে স্বাধীন।}{7. He is free to use it.}
    \exampleitem{৮. আপনি যেকোনো সময় আসতে মুক্ত।}{8. You are free to come anytime.}
    \exampleitem{৯. তারা এটি পরিবর্তন করতে স্বাধীন।}{9. They are free to change it.}
    \exampleitem{১০. আমি তাকে সাহায্য করতে মুক্ত।}{10. I am free to help him.}
\end{examplebox}

% ==========================================
% RULE 87
% ==========================================
\ruleheader{87.}{আমি ইংরেজিতে কথা বলে আনন্দে আত্মহারা।}{I am overjoyed to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমাকে দেখে আনন্দে আত্মহারা।}{1. I am overjoyed to see you.}
    \exampleitem{২. সে খবরটি শুনে আনন্দে আত্মহারা।}{2. He is overjoyed to hear the news.}
    \exampleitem{৩. তারা পুরস্কারটি পেয়ে আনন্দে আত্মহারা।}{3. They are overjoyed to receive the prize.}
    \exampleitem{৪. তুমি পাস করে আনন্দে আত্মহারা।}{4. You are overjoyed to pass.}
    \exampleitem{৫. আমরা ম্যাচটি জিতে আনন্দে আত্মহারা।}{5. We are overjoyed to win the match.}
    \exampleitem{৬. রিনা চাকরিটি পেয়ে আনন্দে আত্মহারা।}{6. Rina is overjoyed to get the job.}
    \exampleitem{৭. সে উপহারটি পেয়ে আনন্দে আত্মহারা।}{7. He is overjoyed to get the gift.}
    \exampleitem{৮. আপনি সত্যটি জেনে আনন্দে আত্মহারা।}{8. You are overjoyed to know the truth.}
    \exampleitem{৯. তারা সুযোগটি পেয়ে আনন্দে আত্মহারা।}{9. They are overjoyed to get the opportunity.}
    \exampleitem{১০. আমি তোমার সাফল্য দেখে আনন্দে আত্মহারা।}{10. I am overjoyed to see your success.}
\end{examplebox}

% ==========================================
% RULE 88
% ==========================================
\ruleheader{88.}{আমি ইংরেজিতে কথা বলে উল্লসিত।}{I am heartened to speak English.}

\begin{examplebox}
    \exampleitem{১. আমি তোমার কথা শুনে উল্লসিত।}{1. I am heartened to hear your words.}
    \exampleitem{২. সে তার উন্নতি দেখে উল্লসিত।}{2. He is heartened to see his progress.}
    \exampleitem{৩. তারা সাহায্য পেয়ে উল্লসিত।}{3. They are heartened to receive help.}
    \exampleitem{৪. তুমি ফলাফলটি দেখে উল্লসিত।}{4. You are heartened to see the result.}
    \exampleitem{৫. আমরা খবরটি জেনে উল্লসিত।}{5. We are heartened to know the news.}
    \exampleitem{৬. রিনা তাকে সুস্থ হতে দেখে উল্লসিত।}{6. Rina is heartened to see him recover.}
    \exampleitem{৭. সে পরিবর্তনটি লক্ষ্য করে উল্লসিত।}{7. He is heartened to notice the change.}
    \exampleitem{৮. আপনি সমর্থন পেয়ে উল্লসিত।}{8. You are heartened to get support.}
    \exampleitem{৯. তারা তাকে জিততে দেখে উল্লসিত।}{9. They are heartened to see him win.}
    \exampleitem{১০. আমি তোমার সাহস দেখে উল্লসিত।}{10. I am heartened to see your courage.}
\end{examplebox}

% ==========================================
% RULE 89
% ==========================================
\ruleheader{89.}{আমি ইংরেজিতে কথা বলতে দক্ষ।}{I am good at speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি গণিতে দক্ষ।}{1. I am good at mathematics.}
    \exampleitem{২. সে সাঁতারে দক্ষ।}{2. He is good at swimming.}
    \exampleitem{৩. তারা ক্রিকেটে দক্ষ।}{3. They are good at cricket.}
    \exampleitem{৪. তুমি ছবি আঁকায় দক্ষ।}{4. You are good at drawing.}
    \exampleitem{৫. আমরা সমস্যা সমাধানে দক্ষ।}{5. We are good at solving problems.}
    \exampleitem{৬. রিনা রান্নায় দক্ষ।}{6. Rina is good at cooking.}
    \exampleitem{৭. সে গাড়ি চালানোয় দক্ষ।}{7. He is good at driving.}
    \exampleitem{৮. আপনি বিতর্কে দক্ষ।}{8. You are good at debating.}
    \exampleitem{৯. তারা কম্পিউটার ব্যবহার করায় দক্ষ।}{9. They are good at using computers.}
    \exampleitem{১০. আমি গান গাওয়ায় দক্ষ।}{10. I am good at singing.}
\end{examplebox}

% ==========================================
% RULE 90
% ==========================================
\ruleheader{90.}{আমি ইংরেজিতে কথা বলতে কাঁচা / দুর্বল।}{I am dull at speaking English. / I am weak in speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি অংকে কাঁচা।}{1. I am dull at mathematics.}
    \exampleitem{২. সে ব্যাকরণে দুর্বল।}{2. He is weak in grammar.}
    \exampleitem{৩. তারা বিজ্ঞানে কাঁচা।}{3. They are dull at science.}
    \exampleitem{৪. তুমি হাতের লেখায় দুর্বল।}{4. You are weak in handwriting.}
    \exampleitem{৫. আমরা খেলাধুলায় কাঁচা।}{5. We are dull at sports.}
    \exampleitem{৬. রিনা রান্নায় দুর্বল।}{6. Rina is weak in cooking.}
    \exampleitem{৭. সে মুখস্ত করায় কাঁচা।}{7. He is dull at memorizing.}
    \exampleitem{৮. আপনি ইংরেজি বলায় দুর্বল।}{8. You are weak in speaking English.}
    \exampleitem{৯. তারা ইতিহাস বিষয়ে কাঁচা।}{9. They are dull at history.}
    \exampleitem{১০. আমি ছবি আঁকায় দুর্বল।}{10. I am weak in drawing.}
\end{examplebox}
% ==========================================
% RULE 91
% ==========================================
\ruleheader{91.}{ইংরেজি বলা হয়।}{English is spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হয়।}{1. The work is done.}
    \exampleitem{২. চিঠিটি লেখা হয়।}{2. The letter is written.}
    \exampleitem{৩. ফুটবল খেলা হয়।}{3. Football is played.}
    \exampleitem{৪. তাকে ডাকা হয়।}{4. He is called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হয়।}{5. The room is cleaned.}
    \exampleitem{৬. গাড়িটি চালানো হয়।}{6. The car is driven.}
    \exampleitem{৭. বইগুলো বিক্রি করা হয়।}{7. The books are sold.}
    \exampleitem{৮. নিয়মগুলো মানা হয়।}{8. The rules are followed.}
    \exampleitem{৯. সত্যটি বলা হয়।}{9. The truth is told.}
    \exampleitem{১০. গরিবদের সাহায্য করা হয়।}{10. The poor are helped.}
\end{examplebox}

% ==========================================
% RULE 92
% ==========================================
\ruleheader{92.}{ইংরেজি বলা হচ্ছে।}{English is being spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হচ্ছে।}{1. The work is being done.}
    \exampleitem{২. চিঠিটি লেখা হচ্ছে।}{2. The letter is being written.}
    \exampleitem{৩. ফুটবল খেলা হচ্ছে।}{3. Football is being played.}
    \exampleitem{৪. তাকে ডাকা হচ্ছে।}{4. He is being called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হচ্ছে।}{5. The room is being cleaned.}
    \exampleitem{৬. গাড়িটি চালানো হচ্ছে।}{6. The car is being driven.}
    \exampleitem{৭. বইগুলো বিক্রি করা হচ্ছে।}{7. The books are being sold.}
    \exampleitem{৮. রাস্তাটি মেরামত করা হচ্ছে।}{8. The road is being repaired.}
    \exampleitem{৯. সত্যটি বলা হচ্ছে।}{9. The truth is being told.}
    \exampleitem{১০. সমস্যাটি আলোচনা করা হচ্ছে।}{10. The problem is being discussed.}
\end{examplebox}

% ==========================================
% RULE 93
% ==========================================
\ruleheader{93.}{ইংরেজি বলা হয়েছে।}{English has been spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হয়েছে।}{1. The work has been done.}
    \exampleitem{২. চিঠিটি লেখা হয়েছে।}{2. The letter has been written.}
    \exampleitem{৩. ফুটবল খেলা হয়েছে।}{3. Football has been played.}
    \exampleitem{৪. তাকে ডাকা হয়েছে।}{4. He has been called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হয়েছে।}{5. The room has been cleaned.}
    \exampleitem{৬. চোরটিকে ধরা হয়েছে।}{6. The thief has been caught.}
    \exampleitem{৭. বিলটি পরিশোধ করা হয়েছে।}{7. The bill has been paid.}
    \exampleitem{৮. সিদ্ধান্তটি নেওয়া হয়েছে।}{8. The decision has been taken.}
    \exampleitem{৯. সত্যটি প্রকাশ করা হয়েছে।}{9. The truth has been revealed.}
    \exampleitem{১০. গরিবদের সাহায্য করা হয়েছে।}{10. The poor have been helped.}
\end{examplebox}

% ==========================================
% RULE 94
% ==========================================
\ruleheader{94.}{ইংরেজি এক ঘণ্টা ধরে বলা হচ্ছে।}{English has been being spoken for an hour.}

\begin{examplebox}
    \exampleitem{১. এক ঘণ্টা ধরে কাজটি করা হচ্ছে।}{1. The work has been being done for an hour.}
    \exampleitem{২. সকাল থেকে ঘরটি পরিষ্কার করা হচ্ছে।}{2. The room has been being cleaned since morning.}
    \exampleitem{৩. দুই ঘণ্টা ধরে ফুটবল খেলা হচ্ছে।}{3. Football has been being played for two hours.}
    \exampleitem{৪. অনেকক্ষণ ধরে তাকে খোঁজা হচ্ছে।}{4. He has been being searched for a long time.}
    \exampleitem{৫. এক মাস ধরে রাস্তাটি মেরামত করা হচ্ছে।}{5. The road has been being repaired for a month.}
    \exampleitem{৬. সকাল থেকে বিষয়টি আলোচনা করা হচ্ছে।}{6. The matter has been being discussed since morning.}
    \exampleitem{৭. তিন দিন ধরে বাড়িটি রং করা হচ্ছে।}{7. The house has been being painted for three days.}
    \exampleitem{৮. দীর্ঘক্ষণ ধরে বিলটি প্রস্তুত করা হচ্ছে।}{8. The bill has been being prepared for a long time.}
    \exampleitem{৯. এক সপ্তাহ ধরে তথ্য সংগ্রহ করা হচ্ছে।}{9. Information has been being collected for a week.}
    \exampleitem{১০. সকাল থেকে খাবার রান্না করা হচ্ছে।}{10. Food has been being cooked since morning.}
\end{examplebox}

% ==========================================
% RULE 95
% ==========================================
\ruleheader{95.}{ইংরেজি বলা হলো / হয়েছিল।}{English was spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হলো।}{1. The work was done.}
    \exampleitem{২. চিঠিটি লেখা হলো।}{2. The letter was written.}
    \exampleitem{৩. ফুটবল খেলা হলো।}{3. Football was played.}
    \exampleitem{৪. তাকে ডাকা হয়েছিল।}{4. He was called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হয়েছিল।}{5. The room was cleaned.}
    \exampleitem{৬. চোরটিকে ধরা হয়েছিল।}{6. The thief was caught.}
    \exampleitem{৭. বইটি বিক্রি করা হয়েছিল।}{7. The book was sold.}
    \exampleitem{৮. নিয়মগুলো মানা হয়েছিল।}{8. The rules were followed.}
    \exampleitem{৯. সত্যটি বলা হয়েছিল।}{9. The truth was told.}
    \exampleitem{১০. গরিবদের সাহায্য করা হয়েছিল।}{10. The poor were helped.}
\end{examplebox}

% ==========================================
% RULE 96
% ==========================================
\ruleheader{96.}{ইংরেজি বলা হচ্ছিল।}{English was being spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হচ্ছিল।}{1. The work was being done.}
    \exampleitem{২. চিঠিটি লেখা হচ্ছিল।}{2. The letter was being written.}
    \exampleitem{৩. ফুটবল খেলা হচ্ছিল।}{3. Football was being played.}
    \exampleitem{৪. তাকে ডাকা হচ্ছিল।}{4. He was being called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হচ্ছিল।}{5. The room was being cleaned.}
    \exampleitem{৬. গাড়িটি চালানো হচ্ছিল।}{6. The car was being driven.}
    \exampleitem{৭. রাস্তাটি মেরামত করা হচ্ছিল।}{7. The road was being repaired.}
    \exampleitem{৮. আলোচনাটি করা হচ্ছিল।}{8. The discussion was being held.}
    \exampleitem{৯. সত্যটি লুকানো হচ্ছিল।}{9. The truth was being hidden.}
    \exampleitem{১০. সমস্যাটি সমাধান করা হচ্ছিল।}{10. The problem was being solved.}
\end{examplebox}

% ==========================================
% RULE 97
% ==========================================
\ruleheader{97.}{ইংরেজি বলা হয়েছিল (অতীতের আগে)।}{English had been spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হয়েছিল।}{1. The work had been done.}
    \exampleitem{২. চিঠিটি আগেই লেখা হয়েছিল।}{2. The letter had already been written.}
    \exampleitem{৩. ফুটবল খেলা হয়েছিল।}{3. Football had been played.}
    \exampleitem{৪. তাকে ডাকা হয়েছিল।}{4. He had been called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হয়েছিল।}{5. The room had been cleaned.}
    \exampleitem{৬. চোরটিকে আগেই ধরা হয়েছিল।}{6. The thief had already been caught.}
    \exampleitem{৭. বিলটি পরিশোধ করা হয়েছিল।}{7. The bill had been paid.}
    \exampleitem{৮. সিদ্ধান্তটি নেওয়া হয়েছিল।}{8. The decision had been taken.}
    \exampleitem{৯. সত্যটি প্রকাশ করা হয়েছিল।}{9. The truth had been revealed.}
    \exampleitem{১০. খবরটি জানানো হয়েছিল।}{10. The news had been informed.}
\end{examplebox}

% ==========================================
% RULE 98
% ==========================================
\ruleheader{98.}{ইংরেজি এক ঘণ্টা ধরে বলা হচ্ছিল।}{English had been being spoken for an hour.}

\begin{examplebox}
    \exampleitem{১. এক ঘণ্টা ধরে কাজটি করা হচ্ছিল।}{1. The work had been being done for an hour.}
    \exampleitem{২. সকাল থেকে ঘরটি পরিষ্কার করা হচ্ছিল।}{2. The room had been being cleaned since morning.}
    \exampleitem{৩. দুই ঘণ্টা ধরে ফুটবল খেলা হচ্ছিল।}{3. Football had been being played for two hours.}
    \exampleitem{৪. অনেকক্ষণ ধরে তাকে খোঁজা হচ্ছিল।}{4. He had been being searched for a long time.}
    \exampleitem{৫. এক মাস ধরে রাস্তাটি মেরামত করা হচ্ছিল।}{5. The road had been being repaired for a month.}
    \exampleitem{৬. সকাল থেকে বিষয়টি আলোচনা করা হচ্ছিল।}{6. The matter had been being discussed since morning.}
    \exampleitem{৭. তিন দিন ধরে বাড়িটি রং করা হচ্ছিল।}{7. The house had been being painted for three days.}
    \exampleitem{৮. দীর্ঘক্ষণ ধরে বিলটি প্রস্তুত করা হচ্ছিল।}{8. The bill had been being prepared for a long time.}
    \exampleitem{৯. এক সপ্তাহ ধরে তথ্য সংগ্রহ করা হচ্ছিল।}{9. Information had been being collected for a week.}
    \exampleitem{১০. সকাল থেকে খাবার রান্না করা হচ্ছিল।}{10. Food had been being cooked since morning.}
\end{examplebox}

% ==========================================
% RULE 99
% ==========================================
\ruleheader{99.}{ইংরেজি বলা হবে।}{English will be spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হবে।}{1. The work will be done.}
    \exampleitem{২. চিঠিটি লেখা হবে।}{2. The letter will be written.}
    \exampleitem{৩. ফুটবল খেলা হবে।}{3. Football will be played.}
    \exampleitem{৪. তাকে ডাকা হবে।}{4. He will be called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হবে।}{5. The room will be cleaned.}
    \exampleitem{৬. গাড়িটি চালানো হবে।}{6. The car will be driven.}
    \exampleitem{৭. বইগুলো বিক্রি করা হবে।}{7. The books will be sold.}
    \exampleitem{৮. নিয়মগুলো মানা হবে।}{8. The rules will be followed.}
    \exampleitem{৯. সত্যটি বলা হবে।}{9. The truth will be told.}
    \exampleitem{১০. পুরস্কারটি দেওয়া হবে।}{10. The prize will be given.}
\end{examplebox}

% ==========================================
% RULE 100
% ==========================================
\ruleheader{100.}{ইংরেজি বলা হতে থাকবে।}{English will be being spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হতে থাকবে।}{1. The work will be being done.}
    \exampleitem{২. চিঠিটি লেখা হতে থাকবে।}{2. The letter will be being written.}
    \exampleitem{৩. ফুটবল খেলা হতে থাকবে।}{3. Football will be being played.}
    \exampleitem{৪. তাকে ডাকা হতে থাকবে।}{4. He will be being called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হতে থাকবে।}{5. The room will be being cleaned.}
    \exampleitem{৬. গাড়িটি চালানো হতে থাকবে।}{6. The car will be being driven.}
    \exampleitem{৭. বইগুলো বিক্রি করা হতে থাকবে।}{7. The books will be being sold.}
    \exampleitem{৮. রাস্তাটি মেরামত করা হতে থাকবে।}{8. The road will be being repaired.}
    \exampleitem{৯. সত্যটি বলা হতে থাকবে।}{9. The truth will be being told.}
    \exampleitem{১০. সমস্যাটি আলোচনা করা হতে থাকবে।}{10. The problem will be being discussed.}
\end{examplebox}

% ==========================================
% RULE 101
% ==========================================
\ruleheader{101.}{ইংরেজি বলা হয়ে থাকবে।}{English will have been spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হয়ে থাকবে।}{1. The work will have been done.}
    \exampleitem{২. চিঠিটি লেখা হয়ে থাকবে।}{2. The letter will have been written.}
    \exampleitem{৩. ফুটবল খেলা হয়ে থাকবে।}{3. Football will have been played.}
    \exampleitem{৪. তাকে ডাকা হয়ে থাকবে।}{4. He will have been called.}
    \exampleitem{৫. ঘরটি পরিষ্কার করা হয়ে থাকবে।}{5. The room will have been cleaned.}
    \exampleitem{৬. চোরটিকে ধরা হয়ে থাকবে।}{6. The thief will have been caught.}
    \exampleitem{৭. বিলটি পরিশোধ করা হয়ে থাকবে।}{7. The bill will have been paid.}
    \exampleitem{৮. সিদ্ধান্তটি নেওয়া হয়ে থাকবে।}{8. The decision will have been taken.}
    \exampleitem{৯. সত্যটি প্রকাশ করা হয়ে থাকবে।}{9. The truth will have been revealed.}
    \exampleitem{১০. খবরটি জানানো হয়ে থাকবে।}{10. The news will have been informed.}
\end{examplebox}

% ==========================================
% RULE 102
% ==========================================
\ruleheader{102.}{ইংরেজি এক ঘণ্টা ধরে বলা হতে থাকবে।}{English will have been being spoken for an hour.}

\begin{examplebox}
    \exampleitem{১. এক ঘণ্টা ধরে কাজটি করা হতে থাকবে।}{1. The work will have been being done for an hour.}
    \exampleitem{২. সকাল থেকে ঘরটি পরিষ্কার করা হতে থাকবে।}{2. The room will have been being cleaned since morning.}
    \exampleitem{৩. দুই ঘণ্টা ধরে ফুটবল খেলা হতে থাকবে।}{3. Football will have been being played for two hours.}
    \exampleitem{৪. অনেকক্ষণ ধরে তাকে খোঁজা হতে থাকবে।}{4. He will have been being searched for a long time.}
    \exampleitem{৫. এক মাস ধরে রাস্তাটি মেরামত করা হতে থাকবে।}{5. The road will have been being repaired for a month.}
    \exampleitem{৬. সকাল থেকে বিষয়টি আলোচনা করা হতে থাকবে।}{6. The matter will have been being discussed since morning.}
    \exampleitem{৭. তিন দিন ধরে বাড়িটি রং করা হতে থাকবে।}{7. The house will have been being painted for three days.}
    \exampleitem{৮. দীর্ঘক্ষণ ধরে বিলটি প্রস্তুত করা হতে থাকবে।}{8. The bill will have been being prepared for a long time.}
    \exampleitem{৯. এক সপ্তাহ ধরে তথ্য সংগ্রহ করা হতে থাকবে।}{9. Information will have been being collected for a week.}
    \exampleitem{১০. সকাল থেকে খাবার রান্না করা হতে থাকবে।}{10. Food will have been being cooked since morning.}
\end{examplebox}

% ==========================================
% RULE 103
% ==========================================
\ruleheader{103.}{ইংরেজি বলা উচিৎ।}{English should be spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা উচিৎ।}{1. The work should be done.}
    \exampleitem{২. তাকে জানানো উচিৎ।}{2. He should be informed.}
    \exampleitem{৩. নিয়মগুলো মানা উচিৎ।}{3. The rules should be followed.}
    \exampleitem{৪. গরিবদের সাহায্য করা উচিৎ।}{4. The poor should be helped.}
    \exampleitem{৫. সত্যটি বলা উচিৎ।}{5. The truth should be told.}
    \exampleitem{৬. পরিবেশ পরিষ্কার রাখা উচিৎ।}{6. The environment should be kept clean.}
    \exampleitem{৭. সময় নষ্ট করা উচিৎ নয়।}{7. Time should not be wasted.}
    \exampleitem{৮. সমস্যাটি সমাধান করা উচিৎ।}{8. The problem should be solved.}
    \exampleitem{৯. বড়দের সম্মান করা উচিৎ।}{9. Elders should be respected.}
    \exampleitem{১০. আইন অমান্য করা উচিৎ নয়।}{10. The law should not be violated.}
\end{examplebox}

% ==========================================
% RULE 104
% ==========================================
\ruleheader{104.}{ইংরেজি বলা উচিৎ ছিল।}{English should have been spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা উচিৎ ছিল।}{1. The work should have been done.}
    \exampleitem{২. তাকে জানানো উচিৎ ছিল।}{2. He should have been informed.}
    \exampleitem{৩. চিঠিটি পাঠানো উচিৎ ছিল।}{3. The letter should have been sent.}
    \exampleitem{৪. গরিবদের সাহায্য করা উচিৎ ছিল।}{4. The poor should have been helped.}
    \exampleitem{৫. সত্যটি বলা উচিৎ ছিল।}{5. The truth should have been told.}
    \exampleitem{৬. সুযোগটি কাজে লাগানো উচিৎ ছিল।}{6. The opportunity should have been utilized.}
    \exampleitem{৭. সময় নষ্ট করা উচিৎ হয়নি।}{7. Time should not have been wasted.}
    \exampleitem{৮. সমস্যাটি সমাধান করা উচিৎ ছিল।}{8. The problem should have been solved.}
    \exampleitem{৯. তাকে নিমন্ত্রণ করা উচিৎ ছিল।}{9. He should have been invited.}
    \exampleitem{১০. ভুলটি সংশোধন করা উচিৎ ছিল।}{10. The mistake should have been corrected.}
\end{examplebox}

% ==========================================
% RULE 105
% ==========================================
\ruleheader{105.}{ইংরেজি বলা যেতে পারে।}{English can be spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি আজ করা যেতে পারে।}{1. The work can be done today.}
    \exampleitem{২. সমস্যাটি সমাধান করা যেতে পারে।}{2. The problem can be solved.}
    \exampleitem{৩. তাকে সাহায্য করা যেতে পারে।}{3. He can be helped.}
    \exampleitem{৪. নিয়মটি পরিবর্তন করা যেতে পারে।}{4. The rule can be changed.}
    \exampleitem{৫. নতুন পদ্ধতিটি ব্যবহার করা যেতে পারে।}{5. The new method can be used.}
    \exampleitem{৬. বইটি পড়া যেতে পারে।}{6. The book can be read.}
    \exampleitem{৭. এটি সহজেই বোঝা যেতে পারে।}{7. It can be understood easily.}
    \exampleitem{৮. একটি মিটিং ডাকা যেতে পারে।}{8. A meeting can be called.}
    \exampleitem{৯. বিলটি কাল পরিশোধ করা যেতে পারে।}{9. The bill can be paid tomorrow.}
    \exampleitem{১০. এখানে একটি হাসপাতাল তৈরি করা যেতে পারে।}{10. A hospital can be built here.}
\end{examplebox}

% ==========================================
% RULE 106
% ==========================================
\ruleheader{106.}{ইংরেজি বলা হোক।}{Let English be spoken.}

\begin{examplebox}
    \exampleitem{১. কাজটি করা হোক।}{1. Let the work be done.}
    \exampleitem{২. দরজাটি খোলা হোক।}{2. Let the door be opened.}
    \exampleitem{৩. তাকে জানানো হোক।}{3. Let him be informed.}
    \exampleitem{৪. সমস্যাটি সমাধান করা হোক।}{4. Let the problem be solved.}
    \exampleitem{৫. সত্যটি বলা হোক।}{5. Let the truth be told.}
    \exampleitem{৬. গরিবদের সাহায্য করা হোক।}{6. Let the poor be helped.}
    \exampleitem{৭. নিয়মগুলো মানা হোক।}{7. Let the rules be followed.}
    \exampleitem{৮. চিঠিটি পোস্ট করা হোক।}{8. Let the letter be posted.}
    \exampleitem{৯. বিষয়টি আলোচনা করা হোক।}{9. Let the matter be discussed.}
    \exampleitem{১০. তাকে শাস্তি দেওয়া হোক।}{10. Let him be punished.}
\end{examplebox}

% ==========================================
% RULE 107
% ==========================================
\ruleheader{107.}{ইংরেজিতে কথা বলা আমার অভ্যাস।}{Speaking English is my habit. / To speak English is my habit.}

\begin{examplebox}
    \exampleitem{১. সকালে হাঁটা আমার অভ্যাস।}{1. Walking in the morning is my habit.}
    \exampleitem{২. বই পড়া একটি ভালো অভ্যাস।}{2. Reading books is a good habit.}
    \exampleitem{৩. সাঁতার কাটা স্বাস্থ্যের জন্য ভালো।}{3. Swimming is good for health.}
    \exampleitem{৪. বেশি কথা বলা একটা বদ অভ্যাস।}{4. Talking much is a bad habit.}
    \exampleitem{৫. মিথ্যা বলা মহাপাপ।}{5. Telling lies is a great sin.}
    \exampleitem{৬. অন্যদের সাহায্য করা মহৎ কাজ।}{6. Helping others is a noble deed.}
    \exampleitem{৭. সকালে ওঠা স্বাস্থ্যের জন্য উপকারী।}{7. To get up early is beneficial for health.}
    \exampleitem{৮. দারিদ্র্য দূর করা সহজ বিষয় না।}{8. To remove poverty is not an easy matter.}
    \exampleitem{৯. শান্তি প্রতিষ্ঠা করা আমাদের দায়িত্ব।}{9. To establish peace is our responsibility.}
    \exampleitem{১০. ধূমপান করা স্বাস্থ্যের জন্য ক্ষতিকর।}{10. Smoking is injurious to health.}
\end{examplebox}

% ==========================================
% RULE 108
% ==========================================
\ruleheader{108.}{আমার অভ্যাস ইংরেজিতে কথা বলা।}{My habit is speaking English. / My habit is to speak English.}

\begin{examplebox}
    \exampleitem{১. তার লক্ষ্য একজন ডাক্তার হওয়া।}{1. His aim is being a doctor.}
    \exampleitem{২. আমার শখ বই পড়া।}{2. My hobby is reading books.}
    \exampleitem{৩. তার কাজ সমস্যা তৈরি করা।}{3. His job is creating problems.}
    \exampleitem{৪. আমার স্বপ্ন একটি গাড়ি কেনা।}{4. My dream is to buy a car.}
    \exampleitem{৫. তোমার দায়িত্ব সন্তানদের শিক্ষিত করা।}{5. Your duty is educating your children.}
    \exampleitem{৬. আমাদের লক্ষ্য শান্তি প্রতিষ্ঠা করা।}{6. Our aim is to establish peace.}
    \exampleitem{৭. তার উদ্দেশ্য পরীক্ষায় প্রথম হওয়া।}{7. His objective is to stand first in the exam.}
    \exampleitem{৮. আমার কাজ শুধু শেখানো।}{8. My job is just to teach.}
    \exampleitem{৯. তার স্বভাব মিথ্যা বলা।}{9. His nature is telling lies.}
    \exampleitem{১০. আমাদের কাজ গরিবদের সাহায্য করা।}{10. Our work is helping the poor.}
\end{examplebox}

% ==========================================
% RULE 109
% ==========================================
\ruleheader{109.}{আমি ইংরেজিতে কথা বলতে/ বলা পছন্দ করি।}{I like to speak English. / I like speaking English.}

\begin{examplebox}
    \exampleitem{১. আমি বই পড়তে ভালোবাসি।}{1. I love to read books. / I love reading books.}
    \exampleitem{২. সে কথা বলা শুরু করলো।}{2. He started to talk. / He started talking.}
    \exampleitem{৩. তারা খেলা বন্ধ করলো।}{3. They stopped to play. / They stopped playing.}
    \exampleitem{৪. রিনা রান্না করতেই থাকলো।}{4. Rina continued to cook. / Rina continued cooking.}
    \exampleitem{৫. আমি গান শুনতে পছন্দ করি।}{5. I like to listen to music. / I like listening to music.}
    \exampleitem{৬. সে দৌড়ানো শুরু করলো।}{6. He began to run. / He began running.}
    \exampleitem{৭. বৃষ্টি হতে লাগলো।}{7. It started to rain. / It started raining.}
    \exampleitem{৮. তিনি ধূমপান করা ছেড়ে দিয়েছেন।}{8. He gave up smoking.} % Only gerund used with 'give up'
    \exampleitem{৯. আমি সেখানে যাওয়া অপছন্দ করি।}{9. I dislike to go there. / I dislike going there.}
    \exampleitem{১০. সে মিথ্যা বলা ঘৃণা করে।}{10. He hates to tell lies. / He hates telling lies.}
\end{examplebox}

% ==========================================
% RULE 110
% ==========================================
\ruleheader{110.}{ইংরেজি শিখে, আমি ইংরেজিতে কথা বলছি।}{Learning English, I am speaking English. / Having learnt English...}

\begin{examplebox}
    \exampleitem{১. কঠোর পরিশ্রম করে, সে সফল হয়েছে।}{1. Working hard, he has succeeded in life.}
    \exampleitem{২. মনোযোগ দিয়ে পড়ে, তুমি ভালো করবে।}{2. Reading attentively, you will do well.}
    \exampleitem{৩. কাজটি শেষ করে, আমি ঘুমাতে গেলাম।}{3. Finishing the work, I went to sleep.}
    \exampleitem{৪. ইন্টারনেট ব্যবহার করে, আমরা তথ্য জানতে পারি।}{4. Using the internet, we can know information.}
    \exampleitem{৫. দরজাটি খুলে, সে ঘরে প্রবেশ করল।}{5. Opening the door, he entered the room.}
    \exampleitem{৬. খাবার খেয়ে, তারা খেলতে গেল।}{6. Having eaten the food, they went to play.}
    \exampleitem{৭. টাকা পেয়ে, সে খুব খুশি হলো।}{7. Getting the money, he became very happy.}
    \exampleitem{৮. খবরটি শুনে, আমরা অবাক হলাম।}{8. Hearing the news, we were surprised.}
    \exampleitem{৯. তাকে দেখে, আমি দৌড়ে গেলাম।}{9. Seeing him, I ran.}
    \exampleitem{১০. চিঠিটি লিখে, সে সেটি পোস্ট করল।}{10. Having written the letter, he posted it.}
\end{examplebox}
% ==========================================
% RULE 111
% ==========================================
\ruleheader{111.}{ইংরেজিতে কথা বলা ছেলেটা আমার ভাই।}{The boy speaking English is my brother.}

\begin{examplebox}
    \exampleitem{১. রাস্তার উপর হাঁটা লোকটা আমার বাবা।}{1. The man walking on the road is my father.}
    \exampleitem{২. দারিদ্র্য সীমার নিচে বসবাস করা লোকজন একটা শোচনীয় জীবন যাপন করছে।}{2. People living under the poverty line are leading a miserable life.}
    \exampleitem{৩. রাস্তায় ঘুমিয়ে থাকা কুকুরটা ঘেউ ঘেউ করছিল।}{3. The dog sleeping on the road was barking.}
    \exampleitem{৪. মাঠে খেলা করা ছেলেগুলো আমার বন্ধু।}{4. The boys playing in the field are my friends.}
    \exampleitem{৫. রান্নাঘরে রান্না করা মহিলাটি আমার মা।}{5. The woman cooking in the kitchen is my mother.}
    \exampleitem{৬. কাঁদ পড়া শিশুটি ক্ষুধার্ত।}{6. The crying child is hungry.}
    \exampleitem{৭. আকাশে ওড়া পাখিগুলো দেখতে সুন্দর।}{7. The birds flying in the sky look beautiful.}
    \exampleitem{৮. গান গাওয়া মেয়েটি আমার বোন।}{8. The girl singing a song is my sister.}
    \exampleitem{৯. কোণায় দাঁড়িয়ে থাকা লোকটি একজন পুলিশ।}{9. The man standing in the corner is a police officer.}
    \exampleitem{১০. বই পড়া ছাত্রটি খুব মেধাবী।}{10. The student reading a book is very brilliant.}
\end{examplebox}

% ==========================================
% RULE 112
% ==========================================
\ruleheader{112.}{আমি ইংরেজিতে কথা বলতে বলতে সেখানে গেলাম।}{I went there speaking English.}

\begin{examplebox}
    \exampleitem{১. শিশুটা কান্না করতে করতে তার মায়ের কাছে গেলো।}{1. The child went to its mother crying.}
    \exampleitem{২. সে হাসতে হাসতে লোকটাকে গুলি করে হত্যা করেছিলো।}{2. He shot down the man laughing.}
    \exampleitem{৩. তোমার বন্ধু হাঁপাতে হাঁপাতে সেখানে পৌঁছেছিলো।}{3. Your friend reached there panting.}
    \exampleitem{৪. আমি গান গাইতে গাইতে কাজ করছিলাম।}{4. I was working singing a song.}
    \exampleitem{৫. সে কাঁপতে কাঁপতে কথা বলছিল।}{5. He was speaking trembling.}
    \exampleitem{৬. মেয়েটি নাচতে নাচতে ঘরে ঢুকল।}{6. The girl entered the room dancing.}
    \exampleitem{৭. বৃদ্ধ লোকটি খুঁড়িয়ে খুঁড়িয়ে হাঁটছিল।}{7. The old man was walking limping.}
    \exampleitem{৮. তারা গল্প করতে করতে চা খাচ্ছিল।}{8. They were drinking tea gossiping.}
    \exampleitem{৯. পাখিটি উড়তে উড়তে দূরে চলে গেল।}{9. The bird went away flying.}
    \exampleitem{১০. ছেলেটি দৌড়াতে দৌড়াতে স্কুলে গেল।}{10. The boy went to school running.}
\end{examplebox}

% ==========================================
% RULE 113
% ==========================================
\ruleheader{113.}{ইংরেজিতে কথা বলতে হলে, আমাকে ইংরেজি শিখতে হবে।}{To speak English, I have to learn English.}

\begin{examplebox}
    \exampleitem{১. জীবনে প্রতিষ্ঠিত হতে হলে, তোমাকে একজন পরিশ্রমী ছাত্র হতে হবে।}{1. To be established in life, you have to be an industrious student.}
    \exampleitem{২. সন্ত্রাসবাদ দূর করতে হলে, আমাদের সরকারকে কিছু কঠোর পদক্ষেপ গ্রহণ করতে হবে।}{2. To remove terrorism, our government has to take some strict steps.}
    \exampleitem{৩. ভালো রেজাল্ট করতে হলে, তোমাকে কঠোর পড়াশোনা করতে হবে।}{3. To make a good result, you have to study hard.}
    \exampleitem{৪. সুস্থ থাকতে হলে, আমাদের সুষম খাবার খেতে হবে।}{4. To stay healthy, we have to eat a balanced diet.}
    \exampleitem{৫. ওজন কমাতে হলে, তোমাকে ব্যায়াম করতে হবে।}{5. To lose weight, you have to exercise.}
    \exampleitem{৬. চাকরি পেতে হলে, তোমার দক্ষতা বাড়াতে হবে।}{6. To get a job, you have to improve your skills.}
    \exampleitem{৭. টাকা জমাতে হলে, আমাদের খরচ কমাতে হবে।}{7. To save money, we have to reduce our expenses.}
    \exampleitem{৮. সফল হতে হলে, তোমাকে ঝুঁকি নিতে হবে।}{8. To succeed, you have to take risks.}
    \exampleitem{৯. সম্মান পেতে হলে, অন্যদের সম্মান করতে হবে।}{9. To get respect, you have to respect others.}
    \exampleitem{১০. পরীক্ষায় পাস করতে হলে, তাকে বই পড়তে হবে।}{10. To pass the exam, he has to read books.}
\end{examplebox}

% ==========================================
% RULE 114
% ==========================================
\ruleheader{114.}{আমি ইংরেজি শিখছি একটা চাকরি পেতে/পাওয়ার জন্য।}{I am learning English to get a job.}

\begin{examplebox}
    \exampleitem{১. তোমাকে কঠোর পরিশ্রম করতে হবে একটা ভালো চাকরি পেতে।}{1. You have to work hard to get a good job.}
    \exampleitem{২. আমার বন্ধু সংবাদপত্র পড়ে সারা বিশ্বের চলমান বিষয় জানতে।}{2. My friend reads newspapers to know the current affairs of the whole world.}
    \exampleitem{৩. আমাদের প্রতিদিন শারীরিক ব্যায়াম করা উচিৎ সুস্থ থাকতে।}{3. We should take exercise everyday to be healthy.}
    \exampleitem{৪. সে ঢাকা গেছে একটি বই কিনতে।}{4. He went to Dhaka to buy a book.}
    \exampleitem{৫. আমি এখানে এসেছি তোমার সাথে দেখা করতে।}{5. I have come here to meet you.}
    \exampleitem{৬. তারা মাঠে গেছে ফুটবল খেলতে।}{6. They went to the field to play football.}
    \exampleitem{৭. টাকা জমাতে সে একটি ব্যাংক অ্যাকাউন্ট খুলেছে।}{7. He opened a bank account to save money.}
    \exampleitem{৮. পরীক্ষায় ভালো করতে রিনা অনেক পড়ছে।}{8. Rina is studying a lot to do well in the exam.}
    \exampleitem{৯. আমি বাজারে যাচ্ছি কিছু সবজি কিনতে।}{9. I am going to the market to buy some vegetables.}
    \exampleitem{১০. সে সাহায্য চাইতে আমার কাছে এসেছিল।}{10. He came to me to ask for help.}
\end{examplebox}

% ==========================================
% RULE 115
% ==========================================
\ruleheader{115.}{ইংরেজি একটা শেখার বিষয়।}{English is a learning matter.}

\begin{examplebox}
    \exampleitem{১. তুমি আমার পড়ার রুমে কী করছো?}{1. What are you doing in my reading room?}
    \exampleitem{২. এটাই আমাদের খেলার মাঠ যেখানে আমরা প্রতিদিন ক্রিকেট খেলি।}{2. This is our playing field where we play cricket everyday.}
    \exampleitem{৩. তোমার পড়ার টেবিলটা কোথায়?}{3. Where is your reading table?}
    \exampleitem{৪. এটা একটা বসার ঘর।}{4. This is a sitting room.}
    \exampleitem{৫. হাঁটার ছড়িটি দরজার পাশে।}{5. The walking stick is beside the door.}
    \exampleitem{৬. এটি একটি খাবার টেবিল।}{6. This is a dining table.}
    \exampleitem{৭. সাঁতার কাটার পুলটি খুব বড়।}{7. The swimming pool is very big.}
    \exampleitem{৮. আমাকে কিছু লেখার কাগজ দাও।}{8. Give me some writing paper.}
    \exampleitem{৯. তার একটি ড্রাইভিং লাইসেন্স দরকার।}{9. He needs a driving license.}
    \exampleitem{১০. আমি একটি সেলাই মেশিন কিনেছি।}{10. I bought a sewing machine.}
\end{examplebox}

% ==========================================
% RULE 116
% ==========================================
\ruleheader{116.}{এটা একটা শেখা বিষয়।}{It is a learnt matter.}

\begin{examplebox}
    \exampleitem{১. সে একটা ব্যবহৃত মোবাইল ফোন কিনবে না।}{1. He will not buy a used mobile phone.}
    \exampleitem{২. সে অত্যাচারিত লোকদেরকে সাহায্য করেছিলো।}{2. He helped the oppressed people.}
    \exampleitem{৩. হতাশাগ্রস্ত লোক জীবনে কোন কিছুই করতে পারে না।}{3. Frustrated people cannot do anything in life.}
    \exampleitem{৪. ভাঙা গ্লাসটি টেবিলের উপর আছে।}{4. The broken glass is on the table.}
    \exampleitem{৫. আমি একটি লেখা চিঠি পেয়েছি।}{5. I received a written letter.}
    \exampleitem{৬. সে ছেঁড়া কাপড় পরতে পছন্দ করে না।}{6. He doesn't like to wear torn clothes.}
    \exampleitem{৭. চুরি যাওয়া গাড়িটি পুলিশ খুঁজে পেয়েছে।}{7. The police found the stolen car.}
    \exampleitem{৮. এটি একটি পরীক্ষিত পদ্ধতি।}{8. This is a tested method.}
    \exampleitem{৯. তারা একটি পরিকল্পিত সিদ্ধান্ত নিয়েছিল।}{9. They took a planned decision.}
    \exampleitem{১০. লুকানো সত্য একদিন প্রকাশ পাবে।}{10. The hidden truth will be revealed one day.}
\end{examplebox}

% ==========================================
% RULE 117
% ==========================================
\ruleheader{117.}{ইংরেজি একটি গুরুত্বপূর্ণ ভাষা।}{English is an important language.}

\begin{examplebox}
    \exampleitem{১. ঢাকা একটি বড় শহর।}{1. Dhaka is a big city.}
    \exampleitem{২. গোলাপ একটি সুন্দর ফুল।}{2. The rose is a beautiful flower.}
    \exampleitem{৩. লোহা একটি দরকারী ধাতু।}{3. Iron is a useful metal.}
    \exampleitem{৪. সে একজন সৎ মানুষ।}{4. He is an honest man.}
    \exampleitem{৫. এটি একটি ভালো বই।}{5. This is a good book.}
    \exampleitem{৬. রিনা একজন মেধাবী ছাত্রী।}{6. Rina is a brilliant student.}
    \exampleitem{৭. বাঘ একটি শক্তিশালী প্রাণী।}{7. The tiger is a strong animal.}
    \exampleitem{৮. স্বাস্থ্য একটি বড় সম্পদ।}{8. Health is a great wealth.}
    \exampleitem{৯. পানি একটি প্রয়োজনীয় উপাদান।}{9. Water is an essential element.}
    \exampleitem{১০. সময় একটি মূল্যবান জিনিস।}{10. Time is a valuable thing.}
\end{examplebox}

% ==========================================
% RULE 118
% ==========================================
\ruleheader{118.}{ইংরেজি বাংলার চেয়ে গুরুত্বপূর্ণ।}{English is more important than Bangla.}

\begin{examplebox}
    \exampleitem{১. সে আমার চেয়ে লম্বা।}{1. He is taller than I.}
    \exampleitem{২. ঢাকা চট্টগ্রামের চেয়ে বড়।}{2. Dhaka is bigger than Chittagong.}
    \exampleitem{৩. এই বইটি ঐ বইটির চেয়ে ভালো।}{3. This book is better than that book.}
    \exampleitem{৪. সোনা রুপার চেয়ে দামী।}{4. Gold is more precious than silver.}
    \exampleitem{৫. রিনা টিনার চেয়ে বেশি বুদ্ধিমতী।}{5. Rina is more intelligent than Tina.}
    \exampleitem{৬. আজকের আবহাওয়া গতকালের চেয়ে গরম।}{6. Today's weather is hotter than yesterday's.}
    \exampleitem{৭. কলম তরবারির চেয়ে শক্তিশালী।}{7. The pen is mightier than the sword.}
    \exampleitem{৮. প্লেন ট্রেনের চেয়ে দ্রুততর।}{8. A plane is faster than a train.}
    \exampleitem{৯. স্বাস্থ্য সম্পদের চেয়ে গুরুত্বপূর্ণ।}{9. Health is more important than wealth.}
    \exampleitem{১০. সে তার ভাইয়ের চেয়ে বেশি পরিশ্রমী।}{10. He is more industrious than his brother.}
\end{examplebox}

% ==========================================
% RULE 119
% ==========================================
\ruleheader{119.}{ইংরেজি সবচেয়ে গুরুত্বপূর্ণ ভাষা।}{English is the most important language.}

\begin{examplebox}
    \exampleitem{১. ঢাকা বাংলাদেশের সবচেয়ে বড় শহর।}{1. Dhaka is the biggest city in Bangladesh.}
    \exampleitem{২. সে ক্লাসের সবচেয়ে ভালো ছাত্র।}{2. He is the best student in the class.}
    \exampleitem{৩. মাউন্ট এভারেস্ট বিশ্বের সর্বোচ্চ পর্বত।}{3. Mount Everest is the highest mountain in the world.}
    \exampleitem{৪. এটি আমার জীবনের সবচেয়ে সুখের দিন।}{4. This is the happiest day of my life.}
    \exampleitem{৫. লোহা সবচেয়ে দরকারী ধাতু।}{5. Iron is the most useful metal.}
    \exampleitem{৬. রিনা পরিবারের সবচেয়ে ছোট মেয়ে।}{6. Rina is the youngest girl in the family.}
    \exampleitem{৭. এটি শহরের সবচেয়ে দামি হোটেল।}{7. This is the most expensive hotel in the city.}
    \exampleitem{৮. নীল তিমি বিশ্বের সবচেয়ে বড় প্রাণী।}{8. The blue whale is the largest animal in the world.}
    \exampleitem{৯. সে গ্রামের সবচেয়ে ধনী মানুষ।}{9. He is the richest man in the village.}
    \exampleitem{১০. প্রশান্ত মহাসাগর সবচেয়ে গভীর মহাসাগর।}{10. The Pacific is the deepest ocean.}
\end{examplebox}

% ==========================================
% RULE 120
% ==========================================
\ruleheader{120.}{ইংরেজি সবচেয়ে গুরুত্বপূর্ণ ভাষাগুলোর মধ্যে একটি।}{English is one of the most important languages.}

\begin{examplebox}
    \exampleitem{১. ঢাকা বিশ্বের সবচেয়ে বড় শহরগুলোর মধ্যে একটি।}{1. Dhaka is one of the biggest cities in the world.}
    \exampleitem{২. সে ক্লাসের সবচেয়ে ভালো ছাত্রদের মধ্যে একজন।}{2. He is one of the best students in the class.}
    \exampleitem{৩. নজরুল ইসলাম বাংলাদেশের সবচেয়ে বিখ্যাত কবিদের মধ্যে একজন।}{3. Nazrul Islam is one of the most famous poets in Bangladesh.}
    \exampleitem{৪. লোহা সবচেয়ে দরকারী ধাতুগুলোর মধ্যে একটি।}{4. Iron is one of the most useful metals.}
    \exampleitem{৫. এটি শহরের সবচেয়ে দামি হোটেলগুলোর মধ্যে একটি।}{5. This is one of the most expensive hotels in the city.}
    \exampleitem{৬. রিনা সবচেয়ে মেধাবী ছাত্রীদের মধ্যে একজন।}{6. Rina is one of the most brilliant students.}
    \exampleitem{৭. বাঘ সবচেয়ে শক্তিশালী প্রাণীগুলোর মধ্যে একটি।}{7. The tiger is one of the strongest animals.}
    \exampleitem{৮. এটি বিশ্বের সবচেয়ে সুন্দর জায়গাগুলোর মধ্যে একটি।}{8. This is one of the most beautiful places in the world.}
    \exampleitem{৯. তিনি আমাদের দেশের সবচেয়ে ধনী ব্যক্তিদের মধ্যে একজন।}{9. He is one of the richest persons in our country.}
    \exampleitem{১০. এটি আমার দেখা সবচেয়ে ভালো সিনেমাগুলোর মধ্যে একটি।}{10. This is one of the best movies I have ever seen.}
\end{examplebox}

% ==========================================
% RULE 121
% ==========================================
\ruleheader{121.}{ইংরেজি বাংলার মত গুরুত্বপূর্ণ।}{English is as important as Bangla.}

\begin{examplebox}
    \exampleitem{১. সে আমার মত লম্বা।}{1. He is as tall as I.}
    \exampleitem{২. রিনা টিনার মত বুদ্ধিমতী।}{2. Rina is as intelligent as Tina.}
    \exampleitem{৩. এই বইটি ঐ বইটির মত ভালো।}{3. This book is as good as that book.}
    \exampleitem{৪. আজকের আবহাওয়া গতকালের মত গরম।}{4. Today's weather is as hot as yesterday's.}
    \exampleitem{৫. সে তার ভাইয়ের মত পরিশ্রমী।}{5. He is as industrious as his brother.}
    \exampleitem{৬. ঢাকা চট্টগ্রামের মত ব্যস্ত।}{6. Dhaka is as busy as Chittagong.}
    \exampleitem{৭. রূপা সোনার মত উজ্জ্বল।}{7. Silver is as shiny as gold.}
    \exampleitem{৮. সে বাঘের মত শক্তিশালী।}{8. He is as strong as a tiger.}
    \exampleitem{৯. মেয়েটি গোলাপের মত সুন্দর।}{9. The girl is as beautiful as a rose.}
    \exampleitem{১০. তার মন বরফের মত শীতল।}{10. His mind is as cold as ice.}
\end{examplebox}

% ==========================================
% RULE 122
% ==========================================
\ruleheader{122.}{এমন কোন ভাষা নেই ইংরেজির মত গুরুত্বপূর্ণ।}{No other language is as important as English.}

\begin{examplebox}
    \exampleitem{১. এমন কোন শহর নেই ঢাকার মত বড়।}{1. No other city is as big as Dhaka.}
    \exampleitem{২. এমন কোন ছেলে নেই তার মত ভালো।}{2. No other boy is as good as him.}
    \exampleitem{৩. এমন কোন ধাতু নেই লোহার মত দরকারী।}{3. No other metal is as useful as iron.}
    \exampleitem{৪. এমন কোন দিন নেই আজকের মত গরম।}{4. No other day is as hot as today.}
    \exampleitem{৫. ক্লাসে এমন কোন ছাত্র নেই তার মত মেধাবী।}{5. No other student in the class is as brilliant as him.}
    \exampleitem{৬. এমন কোন পর্বত নেই এভারেস্টের মত উঁচু।}{6. No other mountain is as high as Everest.}
    \exampleitem{৭. এমন কোন প্রাণী নেই নীল তিমির মত বড়।}{7. No other animal is as large as the blue whale.}
    \exampleitem{৮. গ্রামে এমন কোন লোক নেই তার মত ধনী।}{8. No other man in the village is as rich as him.}
    \exampleitem{৯. এমন কোন সমস্যা নেই এর মত কঠিন।}{9. No other problem is as difficult as this.}
    \exampleitem{১০. এমন কোন ফুল নেই গোলাপের মত সুন্দর।}{10. No other flower is as beautiful as the rose.}
\end{examplebox}

% ==========================================
% RULE 123
% ==========================================
\ruleheader{123.}{খুব কম ভাষাই আছে ইংরেজির মত গুরুত্বপূর্ণ।}{Very few languages are as important as English.}

\begin{examplebox}
    \exampleitem{১. খুব কম শহরই আছে ঢাকার মত বড়।}{1. Very few cities are as big as Dhaka.}
    \exampleitem{২. খুব কম ছেলেই আছে তার মত ভালো।}{2. Very few boys are as good as him.}
    \exampleitem{৩. খুব কম ধাতুই আছে লোহার মত দরকারী।}{3. Very few metals are as useful as iron.}
    \exampleitem{৪. খুব কম দেশই আছে জাপানের মত উন্নত।}{4. Very few countries are as developed as Japan.}
    \exampleitem{৫. ক্লাসে খুব কম ছাত্রই আছে তার মত মেধাবী।}{5. Very few students in the class are as brilliant as him.}
    \exampleitem{৬. খুব কম পর্বতশৃঙ্গই আছে এভারেস্টের মত উঁচু।}{6. Very few peaks are as high as Everest.}
    \exampleitem{৭. খুব কম প্রাণীই আছে বাঘের মত শক্তিশালী।}{7. Very few animals are as strong as a tiger.}
    \exampleitem{৮. গ্রামে খুব কম লোকই আছে তার মত ধনী।}{8. Very few men in the village are as rich as him.}
    \exampleitem{৯. খুব কম লেখকই আছে শেক্সপিয়রের মত বিখ্যাত।}{9. Very few writers are as famous as Shakespeare.}
    \exampleitem{১০. খুব কম ফুলই আছে গোলাপের মত সুন্দর।}{10. Very few flowers are as beautiful as the rose.}
\end{examplebox}

% ==========================================
% RULE 124
% ==========================================
\ruleheader{124.}{ইংরেজি যে কোন ভাষার চেয়ে গুরুত্বপূর্ণ।}{English is more important than any other language.}

\begin{examplebox}
    \exampleitem{১. ঢাকা যে কোন শহরের চেয়ে বড়।}{1. Dhaka is bigger than any other city.}
    \exampleitem{২. সে যে কোন ছেলের চেয়ে ভালো।}{2. He is better than any other boy.}
    \exampleitem{৩. লোহা যে কোন ধাতুর চেয়ে দরকারী।}{3. Iron is more useful than any other metal.}
    \exampleitem{৪. এভারেস্ট যে কোন পর্বতের চেয়ে উঁচু।}{4. Everest is higher than any other mountain.}
    \exampleitem{৫. সে ক্লাসের যে কোন ছাত্রের চেয়ে মেধাবী।}{5. He is more brilliant than any other student in the class.}
    \exampleitem{৬. গোলাপ যে কোন ফুলের চেয়ে সুন্দর।}{6. The rose is more beautiful than any other flower.}
    \exampleitem{৭. বাঘ যে কোন প্রাণীর চেয়ে শক্তিশালী।}{7. The tiger is stronger than any other animal.}
    \exampleitem{৮. সে গ্রামের যে কোন লোকের চেয়ে ধনী।}{8. He is richer than any other man in the village.}
    \exampleitem{৯. শেক্সপিয়র যে কোন লেখকের চেয়ে বিখ্যাত।}{9. Shakespeare is more famous than any other writer.}
    \exampleitem{১০. নীল তিমি যে কোন প্রাণীর চেয়ে বড়।}{10. The blue whale is larger than any other animal.}
\end{examplebox}

% ==========================================
% RULE 125
% ==========================================
\ruleheader{125.}{ইংরেজি অন্য অনেক ভাষার চেয়ে গুরুত্বপূর্ণ।}{English is more important than many other languages.}

\begin{examplebox}
    \exampleitem{১. ঢাকা অন্য অনেক শহরের চেয়ে বড়।}{1. Dhaka is bigger than many other cities.}
    \exampleitem{২. সে অন্য অনেক ছেলের চেয়ে ভালো।}{2. He is better than many other boys.}
    \exampleitem{৩. লোহা অন্য অনেক ধাতুর চেয়ে দরকারী।}{3. Iron is more useful than many other metals.}
    \exampleitem{৪. জাপান অন্য অনেক দেশের চেয়ে উন্নত।}{4. Japan is more developed than many other countries.}
    \exampleitem{৫. সে ক্লাসের অন্য অনেক ছাত্রের চেয়ে মেধাবী।}{5. He is more brilliant than many other students in the class.}
    \exampleitem{৬. গোলাপ অন্য অনেক ফুলের চেয়ে সুন্দর।}{6. The rose is more beautiful than many other flowers.}
    \exampleitem{৭. বাঘ অন্য অনেক প্রাণীর চেয়ে শক্তিশালী।}{7. The tiger is stronger than many other animals.}
    \exampleitem{৮. সে গ্রামের অন্য অনেক লোকের চেয়ে ধনী।}{8. He is richer than many other men in the village.}
    \exampleitem{৯. শেক্সপিয়র অন্য অনেক লেখকের চেয়ে বিখ্যাত।}{9. Shakespeare is more famous than many other writers.}
    \exampleitem{১০. এটি অন্য অনেক উপায়ের চেয়ে সহজ।}{10. This is easier than many other ways.}
\end{examplebox}

% ==========================================
% RULE 126
% ==========================================
\ruleheader{126.}{ইংরেজি বেশিরভাগ ভাষার চেয়ে গুরুত্বপূর্ণ।}{English is more important than most other languages.}

\begin{examplebox}
    \exampleitem{১. ঢাকা বেশিরভাগ শহরের চেয়ে বড়।}{1. Dhaka is bigger than most other cities.}
    \exampleitem{২. সে বেশিরভাগ ছেলের চেয়ে ভালো।}{2. He is better than most other boys.}
    \exampleitem{৩. লোহা বেশিরভাগ ধাতুর চেয়ে দরকারী।}{3. Iron is more useful than most other metals.}
    \exampleitem{৪. জাপান বেশিরভাগ দেশের চেয়ে উন্নত।}{4. Japan is more developed than most other countries.}
    \exampleitem{৫. সে ক্লাসের বেশিরভাগ ছাত্রের চেয়ে মেধাবী।}{5. He is more brilliant than most other students in the class.}
    \exampleitem{৬. গোলাপ বেশিরভাগ ফুলের চেয়ে সুন্দর।}{6. The rose is more beautiful than most other flowers.}
    \exampleitem{৭. বাঘ বেশিরভাগ প্রাণীর চেয়ে শক্তিশালী।}{7. The tiger is stronger than most other animals.}
    \exampleitem{৮. সে গ্রামের বেশিরভাগ লোকের চেয়ে ধনী।}{8. He is richer than most other men in the village.}
    \exampleitem{৯. শেক্সপিয়র বেশিরভাগ লেখকের চেয়ে বিখ্যাত।}{9. Shakespeare is more famous than most other writers.}
    \exampleitem{১০. এটি বেশিরভাগ পদ্ধতির চেয়ে কার্যকর।}{10. This is more effective than most other methods.}
\end{examplebox}

% ==========================================
% RULE 127
% ==========================================
\ruleheader{127.}{ইংরেজি অন্য সকল ভাষার চেয়ে গুরুত্বপূর্ণ।}{English is more important than all other languages.}

\begin{examplebox}
    \exampleitem{১. ঢাকা অন্য সকল শহরের চেয়ে বড়।}{1. Dhaka is bigger than all other cities.}
    \exampleitem{২. সে অন্য সকল ছেলের চেয়ে ভালো।}{2. He is better than all other boys.}
    \exampleitem{৩. লোহা অন্য সকল ধাতুর চেয়ে দরকারী।}{3. Iron is more useful than all other metals.}
    \exampleitem{৪. এভারেস্ট অন্য সকল পর্বতের চেয়ে উঁচু।}{4. Everest is higher than all other mountains.}
    \exampleitem{৫. সে ক্লাসের অন্য সকল ছাত্রের চেয়ে মেধাবী।}{5. He is more brilliant than all other students in the class.}
    \exampleitem{৬. গোলাপ অন্য সকল ফুলের চেয়ে সুন্দর।}{6. The rose is more beautiful than all other flowers.}
    \exampleitem{৭. নীল তিমি অন্য সকল প্রাণীর চেয়ে বড়।}{7. The blue whale is larger than all other animals.}
    \exampleitem{৮. সে গ্রামের অন্য সকল লোকের চেয়ে ধনী।}{8. He is richer than all other men in the village.}
    \exampleitem{৯. শেক্সপিয়র অন্য সকল লেখকের চেয়ে বিখ্যাত।}{9. Shakespeare is more famous than all other writers.}
    \exampleitem{১০. এটি অন্য সকল উপায়ের চেয়ে নিরাপদ।}{10. This is safer than all other ways.}
\end{examplebox}

% ==========================================
% RULE 128
% ==========================================
\ruleheader{128.}{ইংরেজি বাংলার চেয়ে কম গুরুত্বপূর্ণ।}{English is less important than Bangla.}

\begin{examplebox}
    \exampleitem{১. সে আমার চেয়ে কম লম্বা।}{1. He is less tall than I.}
    \exampleitem{২. রূপা সোনার চেয়ে কম দামী।}{2. Silver is less precious than gold.}
    \exampleitem{৩. এই বইটি ঐ বইটির চেয়ে কম ভালো।}{3. This book is less good than that book.}
    \exampleitem{৪. আজকের আবহাওয়া গতকালের চেয়ে কম গরম।}{4. Today's weather is less hot than yesterday's.}
    \exampleitem{৫. সে তার ভাইয়ের চেয়ে কম পরিশ্রমী।}{5. He is less industrious than his brother.}
    \exampleitem{৬. শহরটি ঢাকার চেয়ে কম ব্যস্ত।}{6. The city is less busy than Dhaka.}
    \exampleitem{৭. সমস্যাটি আগের চেয়ে কম কঠিন।}{7. The problem is less difficult than before.}
    \exampleitem{৮. সিনেমাটি প্রথমটির চেয়ে কম আকর্ষণীয়।}{8. The movie is less interesting than the first one.}
    \exampleitem{৯. লোহা সোনার চেয়ে কম মূল্যবান।}{9. Iron is less valuable than gold.}
    \exampleitem{১০. সে তার বোনের চেয়ে কম বুদ্ধিমতী।}{10. She is less intelligent than her sister.}
\end{examplebox}

% ==========================================
% RULE 129
% ==========================================
\ruleheader{129.}{ইংরেজি সবচেয়ে কম গুরুত্বপূর্ণ ভাষা।}{English is the least important language.}

\begin{examplebox}
    \exampleitem{১. এটি সবচেয়ে কম দামী ধাতু।}{1. This is the least precious metal.}
    \exampleitem{২. সে ক্লাসের সবচেয়ে কম মেধাবী ছাত্র।}{2. He is the least brilliant student in the class.}
    \exampleitem{৩. এটি শহরের সবচেয়ে কম ব্যস্ত রাস্তা।}{3. This is the least busy road in the city.}
    \exampleitem{৪. আজকের দিনটি সবচেয়ে কম গরম দিন।}{4. Today is the least hot day.}
    \exampleitem{৫. এটি সমস্যার সবচেয়ে কম ক্ষতিকর দিক।}{5. This is the least harmful aspect of the problem.}
    \exampleitem{৬. সে সবচেয়ে কম পরিশ্রমী ছেলে।}{6. He is the least industrious boy.}
    \exampleitem{৭. এটি সবচেয়ে কম আকর্ষণীয় বই।}{7. This is the least interesting book.}
    \exampleitem{৮. তিনি সবচেয়ে কম জনপ্রিয় নেতা।}{8. He is the least popular leader.}
    \exampleitem{৯. এটি সবচেয়ে কম কার্যকর পদ্ধতি।}{9. This is the least effective method.}
    \exampleitem{১০. ঘরটি সবচেয়ে কম আরামদায়ক।}{10. The room is the least comfortable.}
\end{examplebox}
% ==========================================
% RULE 130
% ==========================================
\ruleheader{130.}{বইটা পড়ার পর, আমি ইংরেজিতে কথা বলি।}{After reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. কাজটি শেষ করার পর, আমি ঘুমাবো।}{1. After finishing the work, I will sleep.}
    \exampleitem{২. সেখানে যাওয়ার পর, সে আমাকে কল করেছিল।}{2. After going there, he called me.}
    \exampleitem{৩. ভাত খাওয়ার পর, আমরা খেলতে যাব।}{3. After eating rice, we will go to play.}
    \exampleitem{৪. বইটি পড়ার পর, আমি বিষয়টি বুঝতে পেরেছি।}{4. After reading the book, I understood the matter.}
    \exampleitem{৫. ইংরেজি শেখার পর, সে একটি ভালো চাকরি পেয়েছিল।}{5. After learning English, he got a good job.}
    \exampleitem{৬. চিঠিটি লেখার পর, রিনা সেটি পোস্ট করেছিল।}{6. After writing the letter, Rina posted it.}
    \exampleitem{৭. সত্যটি জানার পর, সে খুব কষ্ট পেয়েছিল।}{7. After knowing the truth, he got very hurt.}
    \exampleitem{৮. স্টেশনে পৌঁছানোর পর, ট্রেনটি ছেড়ে দিল।}{8. After reaching the station, the train left.}
    \exampleitem{৯. সিনেমাটি দেখার পর, আমরা বাড়ি ফিরেছিলাম।}{9. After watching the movie, we returned home.}
    \exampleitem{১০. ওষুধ খাওয়ার পর, সে ভালো বোধ করছে।}{10. After taking medicine, he is feeling better.}
\end{examplebox}

% ==========================================
% RULE 131
% ==========================================
\ruleheader{131.}{বইটা পড়ার আগে/পূর্বে, আমি ইংরেজিতে কথা বলি।}{Before reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. ঘুমানোর আগে, আমি বই পড়ি।}{1. Before sleeping, I read books.}
    \exampleitem{২. কিছু বলার আগে, চিন্তা করো।}{2. Before saying anything, think.}
    \exampleitem{৩. সিদ্ধান্ত নেওয়ার আগে, সব দিক বিবেচনা করো।}{3. Before taking a decision, consider all aspects.}
    \exampleitem{৪. বাইরে যাওয়ার আগে, দরজা বন্ধ করো।}{4. Before going out, close the door.}
    \exampleitem{৫. পরীক্ষা দেওয়ার আগে, সে কঠোর পড়াশোনা করেছিল।}{5. Before taking the exam, he studied hard.}
    \exampleitem{৬. গাড়ি চালানোর আগে, নিয়মগুলো জানা উচিৎ।}{6. Before driving a car, one should know the rules.}
    \exampleitem{৭. খাওয়ার আগে, তোমার হাত ধোয়া উচিৎ।}{7. Before eating, you should wash your hands.}
    \exampleitem{৮. সেখানে যাওয়ার আগে, আমাকে জানিও।}{8. Before going there, inform me.}
    \exampleitem{৯. কাজ শুরু করার আগে, পরিকল্পনা করা দরকার।}{9. Before starting the work, planning is necessary.}
    \exampleitem{১০. ঢাকা যাওয়ার আগে, আমি তার সাথে দেখা করব।}{10. Before going to Dhaka, I will meet him.}
\end{examplebox}

% ==========================================
% RULE 132
% ==========================================
\ruleheader{132.}{বইটা পড়া দ্বারা, আমি ইংরেজিতে কথা বলি।}{By reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. কঠোর পরিশ্রম করার দ্বারা, তুমি সফল হতে পারো।}{1. By working hard, you can be successful.}
    \exampleitem{২. বই পড়ার দ্বারা, আমরা জ্ঞান অর্জন করি।}{2. By reading books, we acquire knowledge.}
    \exampleitem{৩. ব্যায়াম করার দ্বারা, তুমি সুস্থ থাকতে পারো।}{3. By taking exercise, you can stay healthy.}
    \exampleitem{৪. ইংরেজি শেখার দ্বারা, তুমি একটি ভালো চাকরি পেতে পারো।}{4. By learning English, you can get a good job.}
    \exampleitem{৫. সত্য বলার দ্বারা, সে সবার মন জয় করেছিল।}{5. By telling the truth, he won everyone's heart.}
    \exampleitem{৬. সময় নষ্ট করার দ্বারা, তুমি জীবনে ভুগবে।}{6. By wasting time, you will suffer in life.}
    \exampleitem{৭. তাকে সাহায্য করার দ্বারা, আমি আনন্দ পাই।}{7. By helping him, I get pleasure.}
    \exampleitem{৮. প্রতিদিন অনুশীলন করার দ্বারা, সে ভালো খেলোয়াড় হয়েছে।}{8. By practicing everyday, he became a good player.}
    \exampleitem{৯. বেশি গাছ লাগানোর দ্বারা, আমরা পরিবেশ বাঁচাতে পারি।}{9. By planting more trees, we can save the environment.}
    \exampleitem{১০. দ্রুত হাঁটার দ্বারা, আমরা সময়মতো পৌঁছাতে পারি।}{10. By walking fast, we can reach on time.}
\end{examplebox}

% ==========================================
% RULE 133
% ==========================================
\ruleheader{133.}{বইটা পড়া ছাড়া/না পড়ে, আমি ইংরেজিতে কথা বলি।}{Without reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. কঠোর পরিশ্রম না করে, তুমি সফল হতে পারবে না।}{1. Without working hard, you cannot succeed.}
    \exampleitem{২. পড়াশোনা না করে, পরীক্ষায় পাস করা কঠিন।}{2. Without studying, it is difficult to pass the exam.}
    \exampleitem{৩. অনুমতি ছাড়া, তুমি এখানে প্রবেশ করতে পারবে না।}{3. Without taking permission, you cannot enter here.}
    \exampleitem{৪. পানি পান না করে, আমরা বাঁচতে পারি না।}{4. Without drinking water, we cannot live.}
    \exampleitem{৫. ইংরেজি না জেনে, ভালো চাকরি পাওয়া কঠিন।}{5. Without knowing English, it is hard to get a good job.}
    \exampleitem{৬. চিন্তা না করে, কিছু বলো না।}{6. Without thinking, don't say anything.}
    \exampleitem{৭. টিকিট না কিনে, তুমি ট্রেনে উঠতে পারবে না।}{7. Without buying a ticket, you cannot get on the train.}
    \exampleitem{৮. কারণ না জেনে, তাকে দোষ দিও না।}{8. Without knowing the reason, don't blame him.}
    \exampleitem{৯. চেষ্টা না করে, হার মেনো না।}{9. Without trying, don't give up.}
    \exampleitem{১০. চশমা ছাড়া, সে পড়তে পারে না।}{10. Without using glasses, he cannot read.}
\end{examplebox}

% ==========================================
% RULE 134
% ==========================================
\ruleheader{134.}{বইটা পড়ার পাশাপাশি, আমি ইংরেজিতে কথা বলি।}{Besides reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. ইংরেজি শেখার পাশাপাশি, সে ফ্রেঞ্চও শেখে।}{1. Besides learning English, he learns French too.}
    \exampleitem{২. গান গাওয়ার পাশাপাশি, সে ভালো নাচতেও পারে।}{2. Besides singing, she can dance well.}
    \exampleitem{৩. চাকরি করার পাশাপাশি, সে একটি ব্যবসাও করে।}{3. Besides doing a job, he runs a business.}
    \exampleitem{৪. ক্রিকেট খেলার পাশাপাশি, আমরা ফুটবলও খেলি।}{4. Besides playing cricket, we play football too.}
    \exampleitem{৫. বই পড়ার পাশাপাশি, তার ছবি আঁকার শখ আছে।}{5. Besides reading books, he has a hobby of drawing.}
    \exampleitem{৬. গরিবদের সাহায্য করার পাশাপাশি, সে এতিমখানায় টাকা দেয়।}{6. Besides helping the poor, he donates to the orphanage.}
    \exampleitem{৭. টিভি দেখা ছাড়াও, আমি গল্পের বই পড়ি।}{7. Apart from watching TV, I read story books.}
    \exampleitem{৮. মাংস খাওয়ার পাশাপাশি, সে সবজিও খায়।}{8. Besides eating meat, he eats vegetables.}
    \exampleitem{৯. শিক্ষকতা করা ছাড়াও, তিনি একজন লেখক।}{9. Apart from teaching, he is a writer.}
    \exampleitem{১০. ঢাকা যাওয়ার পাশাপাশি, আমি সিলেটেও যাব।}{10. Besides going to Dhaka, I will go to Sylhet too.}
\end{examplebox}

% ==========================================
% RULE 135
% ==========================================
\ruleheader{135.}{বইটা পড়ার সময়, আমি ইংরেজিতে কথা বলি।}{While reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. রাস্তা পার হওয়ার সময়, সতর্ক থেকো।}{1. While crossing the road, be careful.}
    \exampleitem{২. ঘুমানোর সময়, সে স্বপ্ন দেখছিল।}{2. While sleeping, he was dreaming.}
    \exampleitem{৩. টিভি দেখার সময়, আমি খাচ্ছিলাম।}{3. While watching TV, I was eating.}
    \exampleitem{৪. কথা বলার সময়, সে হাসছিল।}{4. While speaking, he was smiling.}
    \exampleitem{৫. পড়ার সময়, মোবাইল ব্যবহার কোরো না।}{5. While reading, don't use the mobile.}
    \exampleitem{৬. গাড়ি চালানোর সময়, ফোনে কথা বলা উচিত নয়।}{6. While driving, one should not talk on the phone.}
    \exampleitem{৭. হাঁটার সময়, সে একটি মানিব্যাগ পেয়েছিল।}{7. While walking, he found a wallet.}
    \exampleitem{৮. খেলার সময়, সে ব্যথা পেয়েছিল।}{8. While playing, he got hurt.}
    \exampleitem{৯. কাজ করার সময়, মনোযোগ দাও।}{9. While working, pay attention.}
    \exampleitem{১০. রান্না করার সময়, মা গান গাইছিলেন।}{10. While cooking, mother was singing.}
\end{examplebox}

% ==========================================
% RULE 136
% ==========================================
\ruleheader{136.}{বইটা পড়ার কারণে, আমি ইংরেজিতে কথা বলি।}{Because of reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. কঠোর পরিশ্রম করার কারণে, সে সফল হয়েছিল।}{1. Because of working hard, he became successful.}
    \exampleitem{২. দেরি করে আসার কারণে, সে ট্রেনটি মিস করেছিল।}{2. Because of coming late, he missed the train.}
    \exampleitem{৩. ভালো খেলার কারণে, তারা ম্যাচটি জিতেছিল।}{3. Because of playing well, they won the match.}
    \exampleitem{৪. সত্য বলার কারণে, তাকে পুরস্কৃত করা হয়েছিল।}{4. Because of telling the truth, he was rewarded.}
    \exampleitem{৫. বৃষ্টি হওয়ার কারণে, আমরা বাইরে যেতে পারিনি।}{5. Because of raining, we could not go out.}
    \exampleitem{৬. বেশি কথা বলার কারণে, সে সমস্যায় পড়েছিল।}{6. Because of talking too much, he fell into trouble.}
    \exampleitem{৭. পড়াশোনা না করার কারণে, সে পরীক্ষায় ফেল করেছিল।}{7. Because of not studying, he failed the exam.}
    \exampleitem{৮. নিয়ম ভাঙার কারণে, তাকে শাস্তি দেওয়া হয়েছিল।}{8. Because of breaking the rule, he was punished.}
    \exampleitem{৯. সাহায্য করার কারণে, আমি তার প্রতি কৃতজ্ঞ।}{9. Because of helping, I am grateful to him.}
    \exampleitem{১০. ভালো গান গাওয়ার কারণে, সে জনপ্রিয় হয়েছে।}{10. Because of singing well, she became popular.}
\end{examplebox}

% ==========================================
% RULE 137
% ==========================================
\ruleheader{137.}{বইটা পড়া সত্ত্বেও, আমি ইংরেজিতে কথা বলি।}{In spite of reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. কঠোর পরিশ্রম করা সত্ত্বেও, সে ফেল করেছিল।}{1. In spite of working hard, he failed.}
    \exampleitem{২. ধনী হওয়া সত্ত্বেও, সে অসুখী।}{2. Despite being rich, he is unhappy.}
    \exampleitem{৩. অসুস্থ থাকা সত্ত্বেও, সে স্কুলে গিয়েছিল।}{3. In spite of being ill, he went to school.}
    \exampleitem{৪. দ্রুত দৌড়ানো সত্ত্বেও, সে বাসটি ধরতে পারেনি।}{4. Despite running fast, he could not catch the bus.}
    \exampleitem{৫. অনেক পড়াশোনা করা সত্ত্বেও, সে ভালো রেজাল্ট করেনি।}{5. In spite of studying a lot, he didn't make a good result.}
    \exampleitem{৬. সত্য জানা সত্ত্বেও, সে চুপ ছিল।}{6. Despite knowing the truth, he remained silent.}
    \exampleitem{৭. ভালো খেলা সত্ত্বেও, তারা ম্যাচটি হেরেছিল।}{7. In spite of playing well, they lost the match.}
    \exampleitem{৮. তাকে সতর্ক করা সত্ত্বেও, সে ভুলটি করেছিল।}{8. Despite warning him, he made the mistake.}
    \exampleitem{৯. বৃষ্টি হওয়া সত্ত্বেও, আমরা খেলতে গিয়েছিলাম।}{9. In spite of raining, we went to play.}
    \exampleitem{১০. যোগ্যতা থাকা সত্ত্বেও, সে চাকরিটি পায়নি।}{10. Despite having qualifications, he didn't get the job.}
\end{examplebox}

% ==========================================
% RULE 138
% ==========================================
\ruleheader{138.}{বইটা পড়ার পরিবর্তে, আমি ইংরেজিতে কথা বলি।}{Instead of reading the book, I speak English.}

\begin{examplebox}
    \exampleitem{১. চা খাওয়ার পরিবর্তে, আমি কফি খাব।}{1. Instead of drinking tea, I will drink coffee.}
    \exampleitem{২. টিভি দেখার পরিবর্তে, চলো পড়তে বসি।}{2. Instead of watching TV, let's sit to read.}
    \exampleitem{৩. ঘুমানোর পরিবর্তে, সে কাজ করছিল।}{3. Instead of sleeping, he was working.}
    \exampleitem{৪. অভিযোগ করার পরিবর্তে, তারা আমাকে সাহায্য করেছিল।}{4. Instead of complaining, they helped me.}
    \exampleitem{৫. বাসে যাওয়ার পরিবর্তে, আমরা হেঁটে গিয়েছিলাম।}{5. Instead of going by bus, we walked.}
    \exampleitem{৬. ইংরেজি শেখার পরিবর্তে, সে ফ্রেঞ্চ শিখছে।}{6. Instead of learning English, he is learning French.}
    \exampleitem{৭. খেলার পরিবর্তে, সে পড়াশোনা করছে।}{7. Instead of playing, he is studying.}
    \exampleitem{৮. কাঁদার পরিবর্তে, পরিস্থিতি মোকাবিলা করো।}{8. Instead of crying, face the situation.}
    \exampleitem{৯. মাংস খাওয়ার পরিবর্তে, সে মাছ খেয়েছিল।}{9. Instead of eating meat, he ate fish.}
    \exampleitem{১০. চুপ থাকার পরিবর্তে, সে প্রতিবাদ করেছিল।}{10. Instead of keeping quiet, he protested.}
\end{examplebox}

% ==========================================
% RULE 139
% ==========================================
\ruleheader{139.}{আমি ইংরেজিতে কথা বলি বইটা পড়ার জন্য/উদ্দেশ্যে।}{I speak English for reading the book.}

\begin{examplebox}
    \exampleitem{১. আমি বইটি কেনার জন্য ঢাকা গিয়েছিলাম।}{1. I went to Dhaka for buying the book.}
    \exampleitem{২. তাকে সাহায্য করার জন্য ধন্যবাদ।}{2. Thank you for helping him.}
    \exampleitem{৩. সে ইংরেজি শেখার জন্য এখানে আসে।}{3. He comes here for learning English.}
    \exampleitem{৪. মিথ্যা বলার জন্য তাকে শাস্তি দেওয়া হয়েছিল।}{4. He was punished for telling a lie.}
    \exampleitem{৫. কাজটি শেষ করার জন্য আমার আরও সময় দরকার।}{5. I need more time for finishing the work.}
    \exampleitem{৬. ভালো রেজাল্ট করার জন্য সে পড়াশোনা করছে।}{6. He is studying for making a good result.}
    \exampleitem{৭. দেরি করার জন্য আমি দুঃখিত।}{7. I am sorry for being late.}
    \exampleitem{৮. আমাদের নিমন্ত্রণ করার জন্য আপনাকে ধন্যবাদ।}{8. Thank you for inviting us.}
    \exampleitem{৯. টাকা উপার্জনের জন্য সে বিদেশে গেছে।}{9. He went abroad for earning money.}
    \exampleitem{১০. সুস্থ থাকার জন্য প্রতিদিন ব্যায়াম করো।}{10. Take exercise daily for keeping healthy.}
\end{examplebox}

% ==========================================
% RULE 140
% ==========================================
\ruleheader{140.}{যখন আমি কলেজে যাই, তখন আমি ইংরেজিতে কথা বলি।}{When I go to college, I speak English.}

\begin{examplebox}
    \exampleitem{১. যখন বৃষ্টি হচ্ছিল, তখন আমি ঘুমাচ্ছিলাম।}{1. When it was raining, I was sleeping.}
    \exampleitem{২. যখন আমি সেখানে পৌঁছালাম, তখন সে চলে গিয়েছিল।}{2. When I reached there, he had left.}
    \exampleitem{৩. যখন সে আসবে, তখন আমরা বের হব।}{3. When he comes, we will go out.}
    \exampleitem{৪. যখন আমি ছোট ছিলাম, তখন আমি গ্রামে থাকতাম।}{4. When I was young, I lived in the village.}
    \exampleitem{৫. যখন সূর্য ওঠে, তখন অন্ধকার দূর হয়।}{5. When the sun rises, darkness disappears.}
    \exampleitem{৬. যখন শিক্ষক ক্লাসে ঢুকলেন, তখন ছাত্ররা উঠে দাঁড়ালো।}{6. When the teacher entered the class, the students stood up.}
    \exampleitem{৭. যখন তুমি ফ্রি থাকবে, তখন আমাকে কল করো।}{7. When you are free, call me.}
    \exampleitem{৮. যখন সে খবরটি শুনলো, তখন সে খুব খুশি হলো।}{8. When he heard the news, he became very happy.}
    \exampleitem{৯. যখন রাত হয়, তখন তারা ঘরে ফেরে।}{9. When it is night, they return home.}
    \exampleitem{১০. যখন আমি বইটি পড়ছিলাম, তখন সে আমাকে ডাকলো।}{10. When I was reading the book, he called me.}
\end{examplebox}

% ==========================================
% RULE 141
% ==========================================
\ruleheader{141.}{যদি আমি কলেজে যাই, তাহলে আমি ইংরেজিতে কথা বলি।}{If I go to college, I speak English.}

\begin{examplebox}
    \exampleitem{১. যদি তুমি আসো, তাহলে আমি যাব।}{1. If you come, I will go.}
    \exampleitem{২. যদি সে কঠোর পরিশ্রম করে, তবে সে সফল হবে।}{2. If he works hard, he will succeed.}
    \exampleitem{৩. যদি বৃষ্টি হয়, তাহলে আমরা খেলব না।}{3. If it rains, we will not play.}
    \exampleitem{৪. যদি তুমি আমাকে ডাকো, আমি সাহায্য করব।}{4. If you call me, I will help.}
    \exampleitem{৫. যদি সে সত্যি বলে, তবে তাকে ক্ষমা করা হবে।}{5. If he tells the truth, he will be forgiven.}
    \exampleitem{৬. যদি তুমি চাও, আমি বইটি দিতে পারি।}{6. If you want, I can give the book.}
    \exampleitem{৭. যদি তুমি ভালো করে পড়ো, তবে পরীক্ষায় পাস করবে।}{7. If you read well, you will pass the exam.}
    \exampleitem{৮. যদি সে সময়মতো পৌঁছায়, তবে ট্রেনটি পাবে।}{8. If he reaches on time, he will catch the train.}
    \exampleitem{৯. যদি তারা আমাদের দাওয়াত দেয়, তবে আমরা যাব।}{9. If they invite us, we will go.}
    \exampleitem{১০. যদি তুমি চেষ্টা করো, তবে তুমি এটি করতে পারবে।}{10. If you try, you can do it.}
\end{examplebox}

% ==========================================
% RULE 142
% ==========================================
\ruleheader{142.}{যদিও আমি ইংরেজি শিখি তবুও আমি ইংরেজিতে কথা বলতে পারি না।}{Though/Although I learn English, I cannot speak English.}

\begin{examplebox}
    \exampleitem{১. যদিও সে গরিব, তবুও সে সৎ।}{1. Though he is poor, he is honest.}
    \exampleitem{২. যদিও আমি তাকে চিনি, তবুও কথা বলি না।}{2. Although I know him, I do not talk.}
    \exampleitem{৩. যদিও বৃষ্টি হচ্ছিল, তবুও সে স্কুলে গিয়েছিল।}{3. Though it was raining, he went to school.}
    \exampleitem{৪. যদিও সে কঠোর পরিশ্রম করেছিল, তবুও সে ফেল করেছিল।}{4. Although he worked hard, he failed.}
    \exampleitem{৫. যদিও তার অনেক টাকা আছে, তবুও সে সুখী নয়।}{5. Though he has a lot of money, he is not happy.}
    \exampleitem{৬. যদিও সে অসুস্থ ছিল, তবুও সে কাজ করেছিল।}{6. Although he was ill, he worked.}
    \exampleitem{৭. যদিও সে দ্রুত দৌড়েছিল, তবুও বাসটি মিস করেছিল।}{7. Though he ran fast, he missed the bus.}
    \exampleitem{৮. যদিও আমরা তাদের দাওয়াত দিয়েছিলাম, তারা আসেনি।}{8. Although we invited them, they didn't come.}
    \exampleitem{৯. যদিও প্রশ্নটি কঠিন ছিল, সে উত্তর দিয়েছিল।}{9. Though the question was difficult, he answered it.}
    \exampleitem{১০. যদিও এটি দামি, আমি এটি কিনব।}{10. Although it is expensive, I will buy it.}
\end{examplebox}

% ==========================================
% RULE 143
% ==========================================
\ruleheader{143.}{সে জানে যে আমি ইংরেজিতে কথা বলি।}{He knows that I speak English.}

\begin{examplebox}
    \exampleitem{১. আমি জানি যে সে একজন ভালো মানুষ।}{1. I know that he is a good man.}
    \exampleitem{২. সে বলেছিল যে সে আগামীকাল আসবে।}{2. He said that he would come tomorrow.}
    \exampleitem{৩. আমি মনে করি যে বাংলাদেশ উন্নতি করছে।}{3. I think that Bangladesh is developing.}
    \exampleitem{৪. তারা বিশ্বাস করে যে আমরা জিতব।}{4. They believe that we will win.}
    \exampleitem{৫. এটা সত্যি যে স্বাস্থ্যই সম্পদ।}{5. It is true that health is wealth.}
    \exampleitem{৬. শিক্ষক আমাদের বলেছিলেন যে পৃথিবী গোল।}{6. The teacher told us that the earth is round.}
    \exampleitem{৭. আমি আশা করি যে তুমি পরীক্ষায় পাস করবে।}{7. I hope that you will pass the exam.}
    \exampleitem{৮. সে বুঝতে পেরেছিল যে সে ভুল করেছিল।}{8. He realized that he had made a mistake.}
    \exampleitem{৯. সবাই জানে যে সে একজন সৎ লোক।}{9. Everyone knows that he is an honest man.}
    \exampleitem{১০. সে প্রতিশ্রুতি দিয়েছিল যে সে আমাকে সাহায্য করবে।}{10. He promised that he would help me.}
\end{examplebox}

% ==========================================
% RULE 144
% ==========================================
\ruleheader{144.}{ইংরেজি এতই গুরুত্বপূর্ণ যে আমি ইংরেজিতে কথা বলি।}{English is so important that I speak English.}

\begin{examplebox}
    \exampleitem{১. লোকটি এতই দুর্বল যে সে হাঁটতে পারে না।}{1. The man is so weak that he cannot walk.}
    \exampleitem{২. চা এতই গরম ছিল যে আমি পান করতে পারিনি।}{2. The tea was so hot that I could not drink it.}
    \exampleitem{৩. সে এতই বোকা যে বিষয়টা বুঝতে পারেনি।}{3. He is so foolish that he could not understand the matter.}
    \exampleitem{৪. আবহাওয়া এতই খারাপ ছিল যে আমরা বাইরে যাইনি।}{4. The weather was so bad that we didn't go out.}
    \exampleitem{৫. বক্সটি এতই ভারী যে সে তুলতে পারছে না।}{5. The box is so heavy that he cannot lift it.}
    \exampleitem{৬. মেয়েটি এতই ছোট যে কথা বলতে পারে না।}{6. The girl is so little that she cannot speak.}
    \exampleitem{৭. প্রশ্নটি এতই কঠিন ছিল যে কেউ উত্তর দিতে পারেনি।}{7. The question was so difficult that nobody could answer.}
    \exampleitem{৮. সে এতই দ্রুত দৌড়েছিল যে আমি তাকে ধরতে পারিনি।}{8. He ran so fast that I could not catch him.}
    \exampleitem{৯. বইটি এতই মজার যে আমি পড়া বন্ধ করতে পারিনি।}{9. The book is so interesting that I couldn't stop reading.}
    \exampleitem{১০. গাড়িটি এতই দামি যে আমি কিনতে পারব না।}{10. The car is so expensive that I cannot buy it.}
\end{examplebox}

% ==========================================
% RULE 145
% ==========================================
\ruleheader{145.}{আমি ইংরেজি শিখছি যাতে আমি ইংরেজিতে কথা বলতে পারি।}{I am learning English so that / in order that I can speak English.}

\begin{examplebox}
    \exampleitem{১. আমরা খাই যাতে আমরা বাঁচতে পারি।}{1. We eat so that we can live.}
    \exampleitem{২. সে কঠোর পরিশ্রম করে যাতে সে জীবনে সফল হতে পারে।}{2. He works hard so that he can succeed in life.}
    \exampleitem{৩. আমি ঢাকা গিয়েছিলাম যাতে আমি বইটি কিনতে পারি।}{3. I went to Dhaka in order that I could buy the book.}
    \exampleitem{৪. দরজাটি বন্ধ করো যাতে কেউ ঢুকতে না পারে।}{4. Close the door so that nobody can enter.}
    \exampleitem{৫. সে দ্রুত হেঁটেছিল যাতে সে ট্রেনটি ধরতে পারে।}{5. He walked fast so that he could catch the train.}
    \exampleitem{৬. আমি সকালে উঠি যাতে আমি ব্যায়াম করতে পারি।}{6. I get up early so that I can take exercise.}
    \exampleitem{৭. তারা টাকা জমাচ্ছে যাতে তারা একটি বাড়ি কিনতে পারে।}{7. They are saving money in order that they can buy a house.}
    \exampleitem{৮. মনোযোগ দিয়ে পড়ো যাতে তুমি পরীক্ষায় পাস করতে পারো।}{8. Read attentively so that you can pass the exam.}
    \exampleitem{৯. সে ইংরেজি শিখছে যাতে সে একটি ভালো চাকরি পায়।}{9. He is learning English so that he may get a good job.}
    \exampleitem{১০. আমি তাকে সাহায্য করেছিলাম যাতে সে সমস্যাটি সমাধান করতে পারে।}{10. I helped him in order that he could solve the problem.}
\end{examplebox}
% ==========================================
% RULE 146
% ==========================================
\ruleheader{146.}{সে এমনভাবে কথা বলে যেন সে সব জানে।}{He speaks as if / as though he knew everything.}

\begin{examplebox}
    \exampleitem{১. সে এমনভাবে হাঁটে যেন সে একজন রাজা।}{1. He walks as if he were a king.}
    \exampleitem{২. সে এমনভাবে আচরণ করে যেন সে একজন পাগল।}{2. He behaves as though he were mad.}
    \exampleitem{৩. মেয়েটি এমনভাবে কাঁদে যেন সে একটি বাচ্চা।}{3. The girl cries as if she were a child.}
    \exampleitem{৪. সে এমনভাবে আদেশ দেয় যেন সে আমার বস।}{4. He orders as though he were my boss.}
    \exampleitem{৫. ছেলেটি এমনভাবে দৌড়ায় যেন সে উড়ছে।}{5. The boy runs as if he were flying.}
    \exampleitem{৬. সে এমনভাবে কথা বলেছিল যেন সে সব জেনেছিল।}{6. He spoke as if he had known everything.}
    \exampleitem{৭. সে এমনভাবে অভিনয় করেছিল যেন সে আমাকে চেনে না।}{7. He acted as though he had not known me.}
    \exampleitem{৮. সে এমনভাবে হাসে যেন সে খুব সুখী।}{8. He smiles as if he were very happy.}
    \exampleitem{৯. তিনি এমনভাবে গল্পটি বলেন যেন তিনি সেখানে ছিলেন।}{9. He tells the story as though he had been there.}
    \exampleitem{১০. সে এমনভাবে তাকায় যেন সে আমাকে মারবে।}{10. He looks as if he would beat me.}
\end{examplebox}

% ==========================================
% RULE 147
% ==========================================
\ruleheader{147.}{সে জানে আমি ইংরেজিতে কথা বলি কি বলি না/বলি কিনা।}{He knows whether I speak English or not.}

\begin{examplebox}
    \exampleitem{১. আমি জানি না সে আসবে কিনা।}{1. I don't know whether he will come or not.}
    \exampleitem{২. সে জিজ্ঞাসা করেছিল আমি যাব কিনা।}{2. He asked whether I would go or not.}
    \exampleitem{৩. তারা নিশ্চিত নয় বৃষ্টি হবে কিনা।}{3. They are not sure whether it will rain or not.}
    \exampleitem{৪. তুমি পাস করবে কিনা তা তোমার উপর নির্ভর করে।}{4. Whether you will pass or not depends on you.}
    \exampleitem{৫. আমি বলতে পারি না সে আমাকে চেনে কিনা।}{5. I cannot say whether he knows me or not.}
    \exampleitem{৬. সে কাজটি শেষ করেছে কিনা আমি জানি না।}{6. I don't know whether he has finished the work or not.}
    \exampleitem{৭. তিনি সন্দেহ করেন আমি সত্য বলছি কিনা।}{7. He doubts whether I am telling the truth or not.}
    \exampleitem{৮. আমি ভাবছি সে আমাকে সাহায্য করবে কিনা।}{8. I am wondering whether he will help me or not.}
    \exampleitem{৯. সে ডাক্তার কিনা আমি নিশ্চিত নই।}{9. I am not sure whether he is a doctor or not.}
    \exampleitem{১০. তুমি রাজি হও বা না হও, আমি যাব।}{10. Whether you agree or not, I will go.}
\end{examplebox}

% ==========================================
% RULE 148
% ==========================================
\ruleheader{148.}{তুমি এবং আমি উভয়েই ইংরেজিতে কথা বলি।}{Both you and I speak English.}

\begin{examplebox}
    \exampleitem{১. রহিম এবং করিম উভয়েই ক্রিকেট খেলতে পারে।}{1. Both Rahim and Karim can play cricket.}
    \exampleitem{২. সে বাংলা এবং ইংরেজি উভয়েই বলতে পারে।}{2. He can speak both Bangla and English.}
    \exampleitem{৩. আমি চা এবং কফি উভয়েই পছন্দ করি।}{3. I like both tea and coffee.}
    \exampleitem{৪. লোকটি বোকা এবং অলস উভয়ই।}{4. The man is both foolish and lazy.}
    \exampleitem{৫. ঢাকা এবং চট্টগ্রাম উভয়েই বড় শহর।}{5. Both Dhaka and Chittagong are big cities.}
    \exampleitem{৬. সে আমাকে একটি বই এবং একটি কলম উভয়েই দিয়েছিল।}{6. He gave me both a book and a pen.}
    \exampleitem{৭. রিনা এবং মিনা উভয়েই স্কুলে যাচ্ছে।}{7. Both Rina and Mina are going to school.}
    \exampleitem{৮. এই গাড়িটি সুন্দর এবং টেকসই উভয়ই।}{8. This car is both beautiful and durable.}
    \exampleitem{৯. শিক্ষক এবং ছাত্র উভয়েই উপস্থিত ছিলেন।}{9. Both the teacher and the student were present.}
    \exampleitem{১০. আমি ফল এবং সবজি উভয়েই খাই।}{10. I eat both fruits and vegetables.}
\end{examplebox}

% ==========================================
% RULE 149
% ==========================================
\ruleheader{149.}{শুধু তুমিই না, আমিও ইংরেজিতে কথা বলি।}{Not only you but also I speak English.}

\begin{examplebox}
    \exampleitem{১. সে শুধু একটি বইই না, একটি কলমও কিনেছিল।}{1. He bought not only a book but also a pen.}
    \exampleitem{২. শুধু রহিমই না, করিমও ক্রিকেট খেলতে পারে।}{2. Not only Rahim but also Karim can play cricket.}
    \exampleitem{৩. সে শুধু বোকা না, অলসও বটে।}{3. He is not only foolish but also lazy.}
    \exampleitem{৪. আমি শুধু চা না, কফিও পছন্দ করি।}{4. I like not only tea but also coffee.}
    \exampleitem{৫. শুধু ঢাকাই না, চট্টগ্রামও একটি বড় শহর।}{5. Not only Dhaka but also Chittagong is a big city.}
    \exampleitem{৬. সে শুধু বাংলাই না, ইংরেজিও বলতে পারে।}{6. He can speak not only Bangla but also English.}
    \exampleitem{৭. শুধু রিনাই না, মিনাও স্কুলে যাচ্ছে।}{7. Not only Rina but also Mina is going to school.}
    \exampleitem{৮. গাড়িটি শুধু সুন্দরই না, টেকসইও বটে।}{8. The car is not only beautiful but also durable.}
    \exampleitem{৯. শুধু শিক্ষকই না, ছাত্রও উপস্থিত ছিল।}{9. Not only the teacher but also the student was present.}
    \exampleitem{১০. সে শুধু আমাকে সাহায্যই করেনি, টাকাও দিয়েছিল।}{10. He not only helped me but also gave me money.}
\end{examplebox}

% ==========================================
% RULE 150
% ==========================================
\ruleheader{150.}{হয় তুমি না হয় আমি ইংরেজিতে কথা বলি।}{Either you or I speak English.}

\begin{examplebox}
    \exampleitem{১. হয় রহিম না হয় করিম ক্রিকেট খেলবে।}{1. Either Rahim or Karim will play cricket.}
    \exampleitem{২. সে হয় বোকা না হয় পাগল।}{2. He is either foolish or mad.}
    \exampleitem{৩. আমি হয় চা না হয় কফি পান করব।}{3. I will drink either tea or coffee.}
    \exampleitem{৪. হয় সে আসবে না হয় আমি যাব।}{4. Either he will come or I will go.}
    \exampleitem{৫. তুমি হয় একটি কলম না হয় একটি পেন্সিল নিতে পারো।}{5. You can take either a pen or a pencil.}
    \exampleitem{৬. সে হয় ডাক্তার না হয় ইঞ্জিনিয়ার হবে।}{6. He will be either a doctor or an engineer.}
    \exampleitem{৭. হয় রিনা না হয় তার ভাই গ্লাসটি ভেঙেছে।}{7. Either Rina or her brother has broken the glass.}
    \exampleitem{৮. লোকটি হয় সৎ না হয় চতুর।}{8. The man is either honest or clever.}
    \exampleitem{৯. আমরা হয় বাসে না হয় ট্রেনে যাব।}{9. We will go either by bus or by train.}
    \exampleitem{১০. হয় তুমি চুপ থাকো না হয় বাইরে যাও।}{10. Either you keep quiet or go out.}
\end{examplebox}

% ==========================================
% RULE 151
% ==========================================
\ruleheader{151.}{সে কিংবা আমি কেউই ইংরেজিতে কথা বলি না।}{Neither he nor I speak English.}

\begin{examplebox}
    \exampleitem{১. রহিম কিংবা করিম কেউই ক্রিকেট খেলবে না।}{1. Neither Rahim nor Karim will play cricket.}
    \exampleitem{২. সে বোকাও না, পাগলও না।}{2. He is neither foolish nor mad.}
    \exampleitem{৩. আমি চা কিংবা কফি কোনটিই পান করব না।}{3. I will drink neither tea nor coffee.}
    \exampleitem{৪. সে আসবেও না, আমাকে কলও করবে না।}{4. He will neither come nor call me.}
    \exampleitem{৫. তুমি কলম কিংবা পেন্সিল কোনটিই নিতে পারবে না।}{5. You can take neither a pen nor a pencil.}
    \exampleitem{৬. সে ডাক্তারও নয়, ইঞ্জিনিয়ারও নয়।}{6. He is neither a doctor nor an engineer.}
    \exampleitem{৭. রিনা কিংবা তার ভাই কেউই গ্লাসটি ভাঙেনি।}{7. Neither Rina nor her brother has broken the glass.}
    \exampleitem{৮. লোকটি সৎও নয়, চতুরও নয়।}{8. The man is neither honest nor clever.}
    \exampleitem{৯. আমরা বাসেও যাব না, ট্রেনেও যাব না।}{9. We will go neither by bus nor by train.}
    \exampleitem{১০. সে বাংলায়ও কথা বলে না, ইংরেজিতেও না।}{10. He speaks neither in Bangla nor in English.}
\end{examplebox}

% ==========================================
% RULE 152
% ==========================================
\ruleheader{152.}{যদি তুমি ইংরেজিতে কথা না বলো তবে তুমি চাকরিটা পাবে না।}{Unless you speak English, you will not get the job.}

\begin{examplebox}
    \exampleitem{১. যদি তুমি কঠোর পরিশ্রম না করো, তুমি ফেল করবে।}{1. Unless you work hard, you will fail.}
    \exampleitem{২. যদি বৃষ্টি না হয়, আমরা খেলতে যাব।}{2. Unless it rains, we will go to play.}
    \exampleitem{৩. যদি সে আমাকে না ডাকে, আমি যাব না।}{3. Unless he calls me, I will not go.}
    \exampleitem{৪. যদি তুমি তাড়াতাড়ি না চলো, তুমি ট্রেনটি মিস করবে।}{4. Unless you walk fast, you will miss the train.}
    \exampleitem{৫. যদি তুমি সত্যি না বলো, আমি তোমাকে বিশ্বাস করব না।}{5. Unless you tell the truth, I will not believe you.}
    \exampleitem{৬. যদি তুমি ওষুধ না খাও, তুমি সুস্থ হবে না।}{6. Unless you take medicine, you will not be cured.}
    \exampleitem{৭. যদি আমি সময় না পাই, আমি আসতে পারব না।}{7. Unless I get time, I cannot come.}
    \exampleitem{৮. যদি সে মনোযোগ না দেয়, সে ভুল করবে।}{8. Unless he pays attention, he will make a mistake.}
    \exampleitem{৯. যদি তুমি অনুমতি না নাও, তুমি ঢুকতে পারবে না।}{9. Unless you take permission, you cannot enter.}
    \exampleitem{১০. যদি আমরা চেষ্টা না করি, আমরা জিততে পারব না।}{10. Unless we try, we cannot win.}
\end{examplebox}

% ==========================================
% RULE 153
% ==========================================
\ruleheader{153.}{আমি ইংরেজিতে কথা বলি যতক্ষণ তুমি না থাকো।}{I speak English until you stay. / I speak English till you stay.}

\begin{examplebox}
    \exampleitem{১. যতক্ষণ না বৃষ্টি থামে, এখানে অপেক্ষা করো।}{1. Wait here until the rain stops.}
    \exampleitem{২. সে আসা পর্যন্ত আমি খেলব।}{2. I will play till he comes.}
    \exampleitem{৩. ডাক্তার আসা পর্যন্ত রোগীর যত্ন নাও।}{3. Take care of the patient until the doctor comes.}
    \exampleitem{৪. আমি ফেরা পর্যন্ত তুমি পড়াশোনা করো।}{4. You study till I return.}
    \exampleitem{৫. যতক্ষণ না তুমি পাস করো, চেষ্টা করতে থাকো।}{5. Keep trying until you pass.}
    \exampleitem{৬. সকাল হওয়া পর্যন্ত আমরা ঘুমিয়েছিলাম।}{6. We slept till it was morning.}
    \exampleitem{৭. যতক্ষণ না সে সত্য বলে, তাকে আটকে রাখো।}{7. Keep him confined until he tells the truth.}
    \exampleitem{৮. কাজ শেষ হওয়া পর্যন্ত আমি অফিসে থাকব।}{8. I will stay in the office till the work is finished.}
    \exampleitem{৯. যতক্ষণ না বাবা অনুমতি দেন, আমি যাব না।}{9. I will not go until father gives permission.}
    \exampleitem{১০. আমি বলা পর্যন্ত তুমি চুপ থাকো।}{10. Keep quiet till I tell you.}
\end{examplebox}

% ==========================================
% RULE 154
% ==========================================
\ruleheader{154.}{আমি ইংরেজিতে কথা বলি যাতে আমি চাকরিটা না হারাই। (হারানোর ভয়ে)}{I speak English lest I should / might lose the job.}

\begin{examplebox}
    \exampleitem{১. দ্রুত হাঁটো যাতে ট্রেনটি মিস না করো।}{1. Walk fast lest you should miss the train.}
    \exampleitem{২. মনোযোগ দিয়ে পড়ো যাতে পরীক্ষায় ফেল না করো।}{2. Read attentively lest you should fail in the exam.}
    \exampleitem{৩. সে সাবধানে হেঁটেছিল যাতে সে পড়ে না যায়।}{3. He walked carefully lest he should fall down.}
    \exampleitem{৪. ছাতা নাও যাতে বৃষ্টিতে ভিজে না যাও।}{4. Take an umbrella lest you might get wet in the rain.}
    \exampleitem{৫. চুপ থাকো যাতে কেউ শুনে না ফেলে।}{5. Keep quiet lest anyone should hear.}
    \exampleitem{৬. সে দৌড়েছিল এই ভয়ে যে সে ধরা পড়ে যায়।}{6. He ran lest he might get caught.}
    \exampleitem{৭. ওষুধ খাও যাতে অসুখ না বাড়ে।}{7. Take medicine lest the illness should increase.}
    \exampleitem{৮. সত্যটা বলো যাতে পরে সমস্যায় না পড়ো।}{8. Tell the truth lest you should fall into trouble later.}
    \exampleitem{৯. টাকা জমাও যাতে ভবিষ্যতে কষ্ট না পাও।}{9. Save money lest you might suffer in the future.}
    \exampleitem{১০. দরজা লক করো যাতে চোর ঢুকতে না পারে।}{10. Lock the door lest a thief should enter.}
\end{examplebox}

% ==========================================
% RULE 155
% ==========================================
\ruleheader{155.}{যেইমাত্র আমি ইংরেজিতে কথা বললাম সেইমাত্র আমি একটি চাকরি পেলাম।}{As soon as I spoke English, I got a job.}

\begin{examplebox}
    \exampleitem{১. যেইমাত্র শিক্ষক ক্লাসে ঢুকলেন, ছাত্ররা উঠে দাঁড়ালো।}{1. As soon as the teacher entered the class, the students stood up.}
    \exampleitem{২. যেইমাত্র সে খবরটি শুনলো, সে কাঁদতে শুরু করলো।}{2. As soon as he heard the news, he started crying.}
    \exampleitem{৩. আমি স্টেশনে পৌঁছাতে না পৌঁছাতেই ট্রেনটি ছেড়ে দিল।}{3. As soon as I reached the station, the train left.}
    \exampleitem{৪. চোরটি পুলিশকে দেখা মাত্রই দৌড়ে পালালো।}{4. As soon as the thief saw the police, he ran away.}
    \exampleitem{৫. যেইমাত্র বৃষ্টি শুরু হলো, আমরা ঘরে ফিরে এলাম।}{5. As soon as the rain started, we returned home.}
    \exampleitem{৬. সে আমাকে দেখা মাত্রই হাসলো।}{6. As soon as he saw me, he smiled.}
    \exampleitem{৭. যেইমাত্র সূর্য উঠলো, কুয়াশা কেটে গেল।}{7. As soon as the sun rose, the fog disappeared.}
    \exampleitem{৮. আমি চিঠিটি পাওয়া মাত্রই উত্তর দেব।}{8. I will reply as soon as I receive the letter.}
    \exampleitem{৯. যেইমাত্র সে তার ভুল বুঝলো, সে ক্ষমা চাইলো।}{9. As soon as he realized his mistake, he apologized.}
    \exampleitem{১০. খেলা শেষ হওয়া মাত্রই আমরা মাঠ ছাড়লাম।}{10. As soon as the match ended, we left the field.}
\end{examplebox}
% ==========================================
% RULE 156
% ==========================================
\ruleheader{156.}{আমি ইংরেজিতে কথা বলতে না বলতেই আমি একটা চাকরি পেলাম।}{No sooner had I spoken English than I got a job.}

\begin{examplebox}
    \exampleitem{১. স্টেশনে পৌঁছাতে না পৌঁছাতেই ট্রেনটি ছেড়ে দিল।}{1. No sooner had I reached the station than the train left.}
    \exampleitem{২. শিক্ষক ক্লাসে ঢুকতে না ঢুকতেই ছাত্ররা উঠে দাঁড়াল।}{2. No sooner had the teacher entered the class than the students stood up.}
    \exampleitem{৩. চোরটি পুলিশকে দেখতে না দেখতেই দৌড়ে পালাল।}{3. No sooner had the thief seen the police than he ran away.}
    \exampleitem{৪. আমি তাকে ডাকতে না ডাকতেই সে চলে এল।}{4. No sooner had I called him than he came.}
    \exampleitem{৫. বৃষ্টি শুরু হতে না হতেই আমরা ঘরে ফিরলাম।}{5. No sooner had the rain started than we returned home.}
    \exampleitem{৬. ডাক্তার আসতে না আসতেই রোগীটি মারা গেল।}{6. No sooner had the doctor arrived than the patient died.}
    \exampleitem{৭. সূর্য উঠতে না উঠতেই কুয়াশা কেটে গেল।}{7. No sooner had the sun risen than the fog disappeared.}
    \exampleitem{৮. বেল বাজতে না বাজতেই পরীক্ষা শুরু হলো।}{8. No sooner had the bell rung than the exam started.}
    \exampleitem{৯. সে খবরটি শুনতে না শুনতেই কাঁদতে লাগল।}{9. No sooner had she heard the news than she started crying.}
    \exampleitem{১০. আমি বইটি খুলতে না খুলতেই কারেন্ট চলে গেল।}{10. No sooner had I opened the book than the power went out.}
\end{examplebox}

% ==========================================
% RULE 157
% ==========================================
\ruleheader{157.}{যদি আমি ইংরেজিতে কথা বলি তবে আমার বাবা সন্তুষ্ট হয়।}{If I speak English, my father gets satisfied.}

\begin{examplebox}
    \exampleitem{১. যদি তুমি বরফ গরম করো, তবে এটি গলে যায়।}{1. If you heat ice, it melts.}
    \exampleitem{২. যদি বৃষ্টি হয়, তবে রাস্তা ভিজে যায়।}{2. If it rains, the road gets wet.}
    \exampleitem{৩. যদি তুমি ভালো খাও, তবে তুমি সুস্থ থাকো।}{3. If you eat well, you stay healthy.}
    \exampleitem{৪. যদি সে এখানে আসে, আমি খুশি হই।}{4. If he comes here, I get happy.}
    \exampleitem{৫. যদি সূর্য ওঠে, তবে অন্ধকার দূর হয়।}{5. If the sun rises, darkness disappears.}
    \exampleitem{৬. যদি তুমি বেশি পড়ো, তবে তুমি বেশি শেখো।}{6. If you read more, you learn more.}
    \exampleitem{৭. যদি আমরা ব্যায়াম করি, আমাদের শরীর ফিট থাকে।}{7. If we take exercise, our body stays fit.}
    \exampleitem{৮. যদি সে মিথ্যা বলে, তবে সবাই তাকে ঘৃণা করে।}{8. If he tells a lie, everyone hates him.}
    \exampleitem{৯. যদি তুমি পানি ফোটাও, তবে এটি বাষ্পে পরিণত হয়।}{9. If you boil water, it turns into vapor.}
    \exampleitem{১০. যদি তুমি পরিশ্রম করো, তবে তুমি উন্নতি করো।}{10. If you work hard, you prosper.}
\end{examplebox}

% ==========================================
% RULE 158
% ==========================================
\ruleheader{158.}{যদি আমি ইংরেজিতে কথা বলি তবে আমার বাবা সন্তুষ্ট হবে।}{If I speak English, my father will get satisfied.}

\begin{examplebox}
    \exampleitem{১. যদি তুমি আসো, আমি যাব।}{1. If you come, I will go.}
    \exampleitem{২. যদি সে পড়ে, তবে সে পাস করবে।}{2. If he reads, he will pass.}
    \exampleitem{৩. যদি তুমি আমাকে ডাকো, আমি তোমাকে সাহায্য করব।}{3. If you call me, I will help you.}
    \exampleitem{৪. যদি বৃষ্টি হয়, তবে আমরা খেলব না।}{4. If it rains, we will not play.}
    \exampleitem{৫. যদি তারা দাওয়াত দেয়, আমরা অনুষ্ঠানে যোগ দেব।}{5. If they invite us, we will join the program.}
    \exampleitem{৬. যদি সে দ্রুত হাঁটে, তবে সে ট্রেনটি ধরতে পারবে।}{6. If he walks fast, he will catch the train.}
    \exampleitem{৭. যদি তুমি চাও, আমি বইটি কিনব।}{7. If you want, I will buy the book.}
    \exampleitem{৮. যদি তুমি সত্যি বলো, তবে আমি তোমাকে ক্ষমা করব।}{8. If you tell the truth, I will forgive you.}
    \exampleitem{৯. যদি সে চেষ্টা করে, তবে সে সফল হবে।}{9. If he tries, he will succeed.}
    \exampleitem{১০. যদি তুমি কাজটি করো, আমি তোমাকে টাকা দেব।}{10. If you do the work, I will pay you.}
\end{examplebox}

% ==========================================
% RULE 159
% ==========================================
\ruleheader{159.}{যদি আমি ইংরেজিতে কথা বলতাম তবে আমার বাবা সন্তুষ্ট হত।}{If I spoke English, my father would get satisfied.}

\begin{examplebox}
    \exampleitem{১. যদি আমি পাখি হতাম, আকাশে উড়তাম।}{1. If I were a bird, I would fly in the sky.}
    \exampleitem{২. যদি সে আসতো, আমি যেতাম।}{2. If he came, I would go.}
    \exampleitem{৩. যদি আমার অনেক টাকা থাকতো, আমি গরিবদের সাহায্য করতাম।}{3. If I had a lot of money, I would help the poor.}
    \exampleitem{৪. যদি আমি তার নাম জানতাম, আমি তোমাকে বলতাম।}{4. If I knew his name, I would tell you.}
    \exampleitem{৫. যদি তুমি আমাকে ডাকতে, আমি আসতাম।}{5. If you called me, I would come.}
    \exampleitem{৬. যদি সে মনোযোগ দিয়ে পড়তো, সে পাস করতো।}{6. If he read attentively, he would pass.}
    \exampleitem{৭. যদি আমি রাজা হতাম, আমি সবার কষ্ট দূর করতাম।}{7. If I were a king, I would remove everyone's sorrow.}
    \exampleitem{৮. যদি তারা চেষ্টা করতো, তারা ম্যাচটি জিততো।}{8. If they tried, they would win the match.}
    \exampleitem{৯. যদি সে সত্য বলতো, আমি তাকে ক্ষমা করতাম।}{9. If he told the truth, I would forgive him.}
    \exampleitem{১০. যদি তুমি চাইতে, আমি বইটি দিতাম।}{10. If you wanted, I would give the book.}
\end{examplebox}

% ==========================================
% RULE 160
% ==========================================
\ruleheader{160.}{যদি আমি ইংরেজিতে কথা বলে থাকতাম তবে আমার বাবা সন্তুষ্ট হতে পারতো।}{If I had spoken English, my father would have got satisfied.}

\begin{examplebox}
    \exampleitem{১. যদি সে আসতো, তবে আমি যেতাম (গিয়ে থাকতাম)।}{1. If he had come, I would have gone.}
    \exampleitem{২. যদি আমি তাকে দেখতাম, তবে আমি তাকে বলতাম।}{2. If I had seen him, I would have told him.}
    \exampleitem{৩. যদি তুমি আমাকে ডাকতে, তবে আমি সাহায্য করতে পারতাম।}{3. If you had called me, I would have helped you.}
    \exampleitem{৪. যদি সে মনোযোগ দিয়ে পড়তো, তবে সে পাস করে থাকতো।}{4. If he had read attentively, he would have passed.}
    \exampleitem{৫. যদি বৃষ্টি না হতো, আমরা খেলতে পারতাম।}{5. If it had not rained, we would have played.}
    \exampleitem{৬. যদি আমি সময় পেতাম, আমি কাজটি করে থাকতাম।}{6. If I had got time, I would have done the work.}
    \exampleitem{৭. যদি তারা দ্রুত দৌড়াতো, তবে বাসটি ধরতে পারতো।}{7. If they had run fast, they would have caught the bus.}
    \exampleitem{৮. যদি তুমি আগে জানাতে, তবে আমরা ব্যবস্থা নিতাম।}{8. If you had informed earlier, we would have taken measures.}
    \exampleitem{৯. যদি সে সতর্ক থাকতো, তবে দুর্ঘটনাটি ঘটতো না।}{9. If he had been careful, the accident would not have happened.}
    \exampleitem{১০. যদি আমি জানতাম সে অসুস্থ, আমি তাকে দেখতে যেতাম।}{10. If I had known he was ill, I would have gone to see him.}
\end{examplebox}

% ==========================================
% RULE 161
% ==========================================
\ruleheader{161.}{আমি ইংরেজিতে কথা বলি যতক্ষণ তুমি আমার পাশে থাকো।}{I speak English as long as you stay beside me.}

\begin{examplebox}
    \exampleitem{১. আমি তোমার সাথে থাকব যতক্ষণ তুমি চাও।}{1. I will stay with you as long as you want.}
    \exampleitem{২. তুমি এখানে খেলতে পারো যতক্ষণ বৃষ্টি না আসে।}{2. You can play here as long as it doesn't rain.}
    \exampleitem{৩. সে কাজ করবে যতক্ষণ তার শরীরে শক্তি আছে।}{3. He will work as long as he has energy in his body.}
    \exampleitem{৪. আমরা নিরাপদ যতক্ষণ আমরা একতাবদ্ধ।}{4. We are safe as long as we are united.}
    \exampleitem{৫. তুমি টিভি দেখতে পারো যতক্ষণ তুমি তোমার পড়া শেষ করো।}{5. You can watch TV as long as you finish your study.}
    \exampleitem{৬. সে খুশি থাকবে যতক্ষণ তুমি তাকে সাহায্য করবে।}{6. He will be happy as long as you help him.}
    \exampleitem{৭. আমি তোমাকে মনে রাখব যতক্ষণ আমি বেঁচে আছি।}{7. I will remember you as long as I live.}
    \exampleitem{৮. তুমি বইটি রাখতে পারো যতক্ষণ তোমার দরকার।}{8. You can keep the book as long as you need.}
    \exampleitem{৯. তারা অপেক্ষা করবে যতক্ষণ তুমি ফিরে না আসো।}{9. They will wait as long as you don't return.}
    \exampleitem{১০. আমরা হাসব যতক্ষণ আমাদের মন চাইবে।}{10. We will laugh as long as our mind wants.}
\end{examplebox}

% ==========================================
% RULE 162
% ==========================================
\ruleheader{162.}{এখনই আমার ইংরেজিতে কথা বলার উপযুক্ত সময়।}{It is high time I spoke English.}

\begin{examplebox}
    \exampleitem{১. এখনই আমাদের সিদ্ধান্ত নেওয়ার উপযুক্ত সময়।}{1. It is high time we took a decision.}
    \exampleitem{২. এখনই তোমার পড়াশোনা শুরু করার উপযুক্ত সময়।}{2. It is high time you started studying.}
    \exampleitem{৩. এখনই আমাদের খারাপ অভ্যাস ত্যাগ করার উপযুক্ত সময়।}{3. It is high time we gave up bad habits.}
    \exampleitem{৪. এখনই তার চাকরি খোঁজার উপযুক্ত সময়।}{4. It is high time he searched for a job.}
    \exampleitem{৫. এখনই আমাদের দুর্নীতি বন্ধ করার উপযুক্ত সময়।}{5. It is high time we stopped corruption.}
    \exampleitem{৬. এখনই তোমার সত্য বলার উপযুক্ত সময়।}{6. It is high time you told the truth.}
    \exampleitem{৭. এখনই তাদের কাজ শেষ করার উপযুক্ত সময়।}{7. It is high time they finished the work.}
    \exampleitem{৮. এখনই আমাদের বাড়ি ফেরার উপযুক্ত সময়।}{8. It is high time we returned home.}
    \exampleitem{৯. এখনই সরকারের পদক্ষেপ নেওয়ার উপযুক্ত সময়।}{9. It is high time the government took steps.}
    \exampleitem{১০. এখনই তোমার ধূমপান ছাড়ার উপযুক্ত সময়।}{10. It is high time you quit smoking.}
\end{examplebox}

% ==========================================
% RULE 163
% ==========================================
\ruleheader{163.}{আমি ইংরেজিতেই কথা বলতে পারি না, আর স্প্যানিশ তো দূরের কথা।}{I cannot speak English, let alone Spanish.}

\begin{examplebox}
    \exampleitem{১. সে হাঁটতেই পারে না, আবার দৌড়ানো তো দূরের কথা।}{1. He cannot walk, let alone run.}
    \exampleitem{২. আমি একটি সাইকেলই কিনতে পারি না, গাড়ি তো দূরের কথা।}{2. I cannot buy a bicycle, let alone a car.}
    \exampleitem{৩. সে পরীক্ষায় পাসই করতে পারে না, আবার এ+ তো দূরের কথা।}{3. He cannot pass the exam, let alone get A+.}
    \exampleitem{৪. তারা এক মাইলই হাঁটতে পারে না, দশ মাইল তো দূরের কথা।}{4. They cannot walk one mile, let alone ten miles.}
    \exampleitem{৫. আমি বাংলাই ভালো করে জানি না, আবার ফ্রেঞ্চ তো দূরের কথা।}{5. I don't know Bangla well, let alone French.}
    \exampleitem{৬. সে নিজের নামই লিখতে পারে না, আবার চিঠি লেখা তো দূরের কথা।}{6. He cannot write his own name, let alone write a letter.}
    \exampleitem{৭. আমি একশ টাকাই জোগাড় করতে পারি না, এক লক্ষ টাকা তো দূরের কথা।}{7. I cannot manage one hundred taka, let alone one lakh taka.}
    \exampleitem{৮. সে চা-ই বানাতে পারে না, বিরিয়ানি তো দূরের কথা।}{8. She cannot make tea, let alone biryani.}
    \exampleitem{৯. ছেলেটি একটি বইই পড়ে না, আবার লাইব্রেরি তৈরি তো দূরের কথা।}{9. The boy doesn't read a book, let alone build a library.}
    \exampleitem{১০. আমি তাকে চিনিই না, তার বন্ধু হওয়া তো দূরের কথা।}{10. I don't even know him, let alone be his friend.}
\end{examplebox}

% ==========================================
% RULE 164
% ==========================================
\ruleheader{164.}{আমি ইংরেজিতে কথা বলি, শুধুমাত্র যদি তুমি আমার পাশে থাকো।}{I speak English, provided that you are beside me.}

\begin{examplebox}
    \exampleitem{১. আমি তোমাকে সাহায্য করব, শুধুমাত্র যদি তুমি সত্য বলো।}{1. I will help you, provided that you tell the truth.}
    \exampleitem{২. সে পরীক্ষায় পাস করবে, এই শর্তে যে সে পড়াশোনা করে।}{2. He will pass the exam, provided that he studies.}
    \exampleitem{৩. আমরা খেলতে যাব, শুধুমাত্র যদি বৃষ্টি না হয়।}{3. We will go to play, provided that it doesn't rain.}
    \exampleitem{৪. তুমি বইটি নিতে পারো, এই শর্তে যে তুমি এটি কাল ফেরত দেবে।}{4. You can take the book, provided that you return it tomorrow.}
    \exampleitem{৫. তারা কাজটি শেষ করবে, শুধুমাত্র যদি তুমি তাদের টাকা দাও।}{5. They will finish the work, provided that you pay them.}
    \exampleitem{৬. আমি সেখানে যাব, এই শর্তে যে সে আমাকে আমন্ত্রণ জানায়।}{6. I will go there, provided that he invites me.}
    \exampleitem{৭. তুমি গাড়িটি চালাতে পারো, শুধুমাত্র যদি তুমি সাবধানে চালাও।}{7. You can drive the car, provided that you drive carefully.}
    \exampleitem{৮. সরকার সাহায্য করবে, এই শর্তে যে তোমরা ঐক্যবদ্ধ থাকো।}{8. The government will help, provided that you stay united.}
    \exampleitem{৯. সে চাকরিটি পাবে, শুধুমাত্র যদি তার দক্ষতা থাকে।}{9. He will get the job, provided that he has skills.}
    \exampleitem{১০. আমি তোমার সাথে একমত হব, এই শর্তে যে তুমি প্রমাণ দাও।}{10. I will agree with you, provided that you give proof.}
\end{examplebox}

% ==========================================
% RULE 165
% ==========================================
\ruleheader{165.}{তুমি এখানে আসার আগে আমি ইংরেজিতে কথা বলেছিলাম।}{I had spoken English before you came here.}

\begin{examplebox}
    \exampleitem{১. ডাক্তার আসার আগে রোগীটি মারা গিয়েছিল।}{1. The patient had died before the doctor came.}
    \exampleitem{২. ডাক্তার আসার পর রোগীটি মারা গিয়েছিল।}{2. The patient died after the doctor had come.}
    \exampleitem{৩. আমি স্টেশনে পৌঁছানোর আগে ট্রেনটি ছেড়ে দিয়েছিল।}{3. The train had left before I reached the station.}
    \exampleitem{৪. আমি স্টেশনে পৌঁছানোর পর ট্রেনটি ছেড়ে দিয়েছিল।}{4. The train left after I had reached the station.}
    \exampleitem{৫. শিক্ষক ক্লাসে প্রবেশের আগে ছাত্ররা উঠে দাঁড়িয়েছিল।}{5. The students had stood up before the teacher entered the class.}
    \exampleitem{৬. শিক্ষক ক্লাসে প্রবেশের পর ছাত্ররা উঠে দাঁড়িয়েছিল।}{6. The students stood up after the teacher had entered the class.}
    \exampleitem{৭. ঘণ্টা বাজার আগে আমরা পরীক্ষা শেষ করেছিলাম।}{7. We had finished the exam before the bell rang.}
    \exampleitem{৮. সূর্য ওঠার আগে তারা কাজ শুরু করেছিল।}{8. They had started the work before the sun rose.}
    \exampleitem{৯. সে যাওয়ার পর আমি সেখানে পৌঁছেছিলাম।}{9. I reached there after he had gone.}
    \exampleitem{১০. আমরা পৌঁছানোর আগে তারা খেলা শুরু করেছিল।}{10. They had started playing before we reached.}
\end{examplebox}

% ==========================================
% RULE 166
% ==========================================
\ruleheader{166.}{আমি ইংরেজিতে এতোটাই দুর্বল যে ইংরেজিতে কথা বলতে পারি না।}{I am too weak in English to speak.}

\begin{examplebox}
    \exampleitem{১. লোকটি এতোটাই দুর্বল যে হাঁটতে পারে না।}{1. The man is too weak to walk.}
    \exampleitem{২. চা এতোটাই গরম যে পান করা যায় না।}{2. The tea is too hot to drink.}
    \exampleitem{৩. সে এতোটাই বোকা যে বিষয়টা বুঝতে পারে না।}{3. He is too foolish to understand the matter.}
    \exampleitem{৪. বক্সটি এতোটাই ভারী যে সে তুলতে পারে না।}{4. The box is too heavy for him to lift.}
    \exampleitem{৫. আবহাওয়া এতোটাই খারাপ যে বাইরে যাওয়া যায় না।}{5. The weather is too bad to go out.}
    \exampleitem{৬. মেয়েটি এতোটাই ছোট যে কথা বলতে পারে না।}{6. The girl is too little to speak.}
    \exampleitem{৭. প্রশ্নটি এতোটাই কঠিন যে উত্তর দেওয়া যায় না।}{7. The question is too difficult to answer.}
    \exampleitem{৮. সে এতোটাই দ্রুত দৌড়ায় যে তাকে ধরা যায় না।}{8. He runs too fast to catch.}
    \exampleitem{৯. গাড়িটি এতোটাই দামি যে আমি কিনতে পারি না।}{9. The car is too expensive for me to buy.}
    \exampleitem{১০. সে এতোটাই ক্লান্ত যে কাজ করতে পারে না।}{10. He is too tired to work.}
\end{examplebox}


\end{document}