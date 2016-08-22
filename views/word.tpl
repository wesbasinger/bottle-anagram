<!DOCTYPE html>
<html>
	<head>
		<title>Anagram Game</title>
	</head>
	<body>
		<h1>Anagram Game</h1>
		<h2>Word: {{ word }}</h2>
		<form action="/word/{{ word }}" method="post">
			<input type="radio" value="True" name="is-anagram"/> Yes
			<input type="radio" value="False" name="is-anagram" /> No
			<input type="submit" value="Check" />
		</form>
	</body>
</html>
