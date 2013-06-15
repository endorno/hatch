INSERT IGNORE into users (user_id,name) values (1,'ban_yuki'),(2,'teppei_fujisawa'),(3,'taro_ziro');

INSERT IGNORE into eggs (user_id,egg_id,challenge,promise,do_when,asin,price,title,thumbnail,detail_link) values
(1,1001,'スケボーを始める','スケボーを買う',30,'0',101,'スケボー','http://hoge.jpg','http://google.com'),
(1,1002,'○○へ美味しいケーキを食べに行く','○○を誘う',5,'0',101,'スケボー','http://hoge.jpg','http://google.com'),
(2,2001,'サバゲーを撮影する','GoProを買う',15,'0',101,'スケボー','http://hoge.jpg','http://google.com'),
(2,2002,'ダイビングに行く','セブ行きのチケットを買う',40,'0',101,'スケボー','http://hoge.jpg','http://google.com'),
(3,3001,'田舎に帰って親孝行','岡山行きの新幹線のチケットを買う',10,'0',101,'スケボー','http://hoge.jpg','http://google.com'),
(3,3002,'世界の熱い人に会って学ぶ','どうしよう',5,'0',101,'スケボー','http://hoge.jpg','http://google.com');

INSERT IGNORE INTO cheers (user_id,egg_id,comment) values
(1,2001,'買えよw'),
(2,1002,'リア充乙ｗ'),
(2,1001,'俺もやりたい！'),
(1,3001,'いいね！'),
(2,3001,'いいね！'),
(3,1001,'いいね！');
