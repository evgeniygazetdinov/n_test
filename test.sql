
CREATE TABLE IF NOT EXISTS page_views(
  	site_id int,
  	view_time timestamp
  );

CREATE TABLE IF NOT EXISTS page_visits(
    site_id int,
    page_id int,
    host_ip inet,
    visit_time timestamp default now()
);
--CREATE INDEX site_id_idx ON page_views (site_id);
--CREATE INDEX visit_time_idx ON page_views USING BRIN (view_time);

--INSERT INTO page_visits VALUES (1, 1, '23.244.194.184');
--INSERT INTO page_visits VALUES (2, 2, '217.94.24.71');
--INSERT INTO page_visits VALUES (3, 3, '78.34.81.40');


--1.
select count(site_id), count(page_id) from page_visits where visit_time < date_trunc('day', NOW() - interval '2 month');
--2
--ALTER TABLE "page_visits" ADD PRIMARY KEY IF NOT EXISTS ("daily_id");
--CREATE TABLE IF NOT EXISTS daily_page_visits(
--  		visits_info_group varchar(25)
--  		foreign key(page_visits_id) references page_visits(daily_id),
--  )
