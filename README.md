# Heulwen_CPMN

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lộng Lẫy 7 Màu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb, #a6c1ee, #fbc2eb, #fad0c4);
            background-size: 400% 400%;
            animation: gradientBackground 10s ease infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        @keyframes gradientBackground {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        h1 {
            font-size: 3rem;
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb, #a6c1ee, #fbc2eb, #fad0c4);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            animation: gradientText 5s ease infinite;
        }
        @keyframes gradientText {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            font-size: 1.5rem;
            margin: 10px 0;
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb, #a6c1ee, #fbc2eb, #fad0c4);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            animation: gradientText 5s ease infinite;
        }
    </style>
</head>
<body>
    <div>
        <h1>Đây là nơi để code Web</h1>
        <ul>
            <li>Name: Châu Bình Nguyên</li>
            <li>Nickname: Heulwen</li>
        </ul>
    </div>
</body>
</html>
