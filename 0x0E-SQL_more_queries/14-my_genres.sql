-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows
SELECT genres.`name` AS name
FROM `tv_genres` AS `genres`
INNER JOIN `tv_show_genres` AS `show_genres`
ON genres.`id` = show_genres.`genre_id`

INNER JOIN `tv_shows` AS `shows`
ON shows.`id` = show_genres.`show_id`

WHERE shows.title = "Dexter"
ORDER BY name;
