
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'allauthdemo' WHERE id=1;


DELETE from auth_user;  -- or just the first user?
INSERT INTO auth_user(id, password, last_login, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES (1, 'pbkdf2_sha256$12000$QQxTUGFFLqLE$9JyXI4WgwyYpmxlL+S1JYGExsCH1QhINeBLR6B8cj/8=', '2015-05-31 12:55:12.775326', 1, 'palansh', 'agarwal', 'palanshagarwal@gmail.com', 1, 1, '2015-05-31 12:55:12.775326');



--
-- Prep for socialapp_sites
--
DELETE FROM socialaccount_socialapp_sites;





--
-- Google
--
DELETE FROM socialaccount_socialapp WHERE provider='google';
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
VALUES ("google", "Google", "123", "123", '');

INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (
  (SELECT id FROM socialaccount_socialapp WHERE provider='google'),1);

