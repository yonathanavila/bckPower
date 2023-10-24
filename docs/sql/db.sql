-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION "admin";

-- DROP SEQUENCE public.auth_group_id_seq;

CREATE SEQUENCE public.auth_group_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_group_permissions_id_seq;

CREATE SEQUENCE public.auth_group_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_permission_id_seq;

CREATE SEQUENCE public.auth_permission_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_groups_id_seq;

CREATE SEQUENCE public.auth_user_groups_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_id_seq;

CREATE SEQUENCE public.auth_user_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.auth_user_user_permissions_id_seq;

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_game_game_pk_seq;

CREATE SEQUENCE public.base_game_game_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_gamedetail_game_detail_pk_seq;

CREATE SEQUENCE public.base_gamedetail_game_detail_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_league_league_pk_seq;

CREATE SEQUENCE public.base_league_league_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_match_match_pk_seq;

CREATE SEQUENCE public.base_match_match_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_matchdetail_match_detail_pk_seq;

CREATE SEQUENCE public.base_matchdetail_match_detail_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_matchmode_match_mode_pk_seq;

CREATE SEQUENCE public.base_matchmode_match_mode_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_matchstate_match_state_pk_seq;

CREATE SEQUENCE public.base_matchstate_match_state_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_matchstrategy_match_strategy_pk_seq;

CREATE SEQUENCE public.base_matchstrategy_match_strategy_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_matchtype_match_type_pk_seq;

CREATE SEQUENCE public.base_matchtype_match_type_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_player_player_pk_seq;

CREATE SEQUENCE public.base_player_player_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_section_section_pk_seq;

CREATE SEQUENCE public.base_section_section_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_sectionname_section_name_pk_seq;

CREATE SEQUENCE public.base_sectionname_section_name_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_stage_stage_pk_seq;

CREATE SEQUENCE public.base_stage_stage_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_stagename_stage_name_pk_seq;

CREATE SEQUENCE public.base_stagename_stage_name_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_stageslug_stage_slug_pk_seq;

CREATE SEQUENCE public.base_stageslug_stage_slug_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_stagetype_stage_type_pk_seq;

CREATE SEQUENCE public.base_stagetype_stage_type_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_team_team_pk_seq;

CREATE SEQUENCE public.base_team_team_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.base_tournament_tournament_pk_seq;

CREATE SEQUENCE public.base_tournament_tournament_pk_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_admin_log_id_seq;

CREATE SEQUENCE public.django_admin_log_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_content_type_id_seq;

CREATE SEQUENCE public.django_content_type_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.django_migrations_id_seq;

CREATE SEQUENCE public.django_migrations_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;-- public.auth_group definition

-- Drop table

-- DROP TABLE public.auth_group;

CREATE TABLE public.auth_group (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	"name" varchar(150) NOT NULL,
	CONSTRAINT auth_group_name_key UNIQUE (name),
	CONSTRAINT auth_group_pkey PRIMARY KEY (id)
);
CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


-- public.auth_user definition

-- Drop table

-- DROP TABLE public.auth_user;

CREATE TABLE public.auth_user (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	"password" varchar(128) NOT NULL,
	last_login timestamptz NULL,
	is_superuser bool NOT NULL,
	username varchar(150) NOT NULL,
	first_name varchar(150) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff bool NOT NULL,
	is_active bool NOT NULL,
	date_joined timestamptz NOT NULL,
	CONSTRAINT auth_user_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_username_key UNIQUE (username)
);
CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


-- public.base_game definition

-- Drop table

-- DROP TABLE public.base_game;

CREATE TABLE public.base_game (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	game_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	game_id int8 NOT NULL,
	game_platform_id varchar(255) NOT NULL,
	game_year int4 NOT NULL,
	CONSTRAINT base_game_game_id_78eab5f6_uniq UNIQUE (game_id),
	CONSTRAINT base_game_pkey PRIMARY KEY (game_pk)
);


-- public.base_league definition

-- Drop table

-- DROP TABLE public.base_league;

CREATE TABLE public.base_league (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	league_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	league_id int8 NOT NULL,
	league_name varchar(255) NOT NULL,
	league_slug varchar(255) NOT NULL,
	league_sport varchar(6) NOT NULL,
	league_image varchar(500) NOT NULL,
	league_light_image varchar(255) NOT NULL,
	league_dark_image varchar(255) NOT NULL,
	league_region varchar(255) NOT NULL,
	league_priority int4 NOT NULL,
	league_display_priority_position int4 NOT NULL,
	league_display_priority_status bool NOT NULL,
	CONSTRAINT base_league_league_id_e52d257a_uniq UNIQUE (league_id),
	CONSTRAINT base_league_pkey PRIMARY KEY (league_pk)
);
CREATE INDEX base_league_league_image_c47305ff ON public.base_league USING btree (league_image);
CREATE INDEX base_league_league_image_c47305ff_like ON public.base_league USING btree (league_image varchar_pattern_ops);
CREATE INDEX base_league_league_slug_055a3208 ON public.base_league USING btree (league_slug);
CREATE INDEX base_league_league_slug_055a3208_like ON public.base_league USING btree (league_slug varchar_pattern_ops);


-- public.base_matchmode definition

-- Drop table

-- DROP TABLE public.base_matchmode;

CREATE TABLE public.base_matchmode (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_mode_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_mode_name varchar(50) NOT NULL,
	CONSTRAINT base_matchmode_pkey PRIMARY KEY (match_mode_pk)
);


-- public.base_matchstate definition

-- Drop table

-- DROP TABLE public.base_matchstate;

CREATE TABLE public.base_matchstate (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_state_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_state_name varchar(50) NOT NULL,
	CONSTRAINT base_matchstate_pkey PRIMARY KEY (match_state_pk)
);


-- public.base_matchstrategy definition

-- Drop table

-- DROP TABLE public.base_matchstrategy;

CREATE TABLE public.base_matchstrategy (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_strategy_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_strategy_name varchar(50) NOT NULL,
	CONSTRAINT base_matchstrategy_pkey PRIMARY KEY (match_strategy_pk)
);


-- public.base_matchtype definition

-- Drop table

-- DROP TABLE public.base_matchtype;

CREATE TABLE public.base_matchtype (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_type_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_type_name varchar(50) NOT NULL,
	CONSTRAINT base_matchtype_pkey PRIMARY KEY (match_type_pk)
);


-- public.base_player definition

-- Drop table

-- DROP TABLE public.base_player;

CREATE TABLE public.base_player (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	player_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	player_id int8 NOT NULL,
	team_id int8 NULL,
	player_handle varchar(16) NOT NULL,
	player_name varchar(255) NOT NULL,
	CONSTRAINT base_player_pkey PRIMARY KEY (player_pk),
	CONSTRAINT base_player_player_id_3c6eb6ee_uniq UNIQUE (player_id)
);


-- public.base_sectionname definition

-- Drop table

-- DROP TABLE public.base_sectionname;

CREATE TABLE public.base_sectionname (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	section_name_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	section_name varchar(50) NOT NULL,
	section_name_name varchar(50) NULL,
	CONSTRAINT base_sectionname_pkey PRIMARY KEY (section_name_pk)
);


-- public.base_stagename definition

-- Drop table

-- DROP TABLE public.base_stagename;

CREATE TABLE public.base_stagename (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	stage_name_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	stage_name_name varchar(50) NOT NULL,
	CONSTRAINT base_stagename_pkey PRIMARY KEY (stage_name_pk)
);


-- public.base_stageslug definition

-- Drop table

-- DROP TABLE public.base_stageslug;

CREATE TABLE public.base_stageslug (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	stage_slug_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	stage_slug_slug varchar(50) NOT NULL,
	CONSTRAINT base_stageslug_pkey PRIMARY KEY (stage_slug_pk)
);


-- public.base_stagetype definition

-- Drop table

-- DROP TABLE public.base_stagetype;

CREATE TABLE public.base_stagetype (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	stage_type_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	stage_type_name varchar(50) NOT NULL,
	CONSTRAINT base_stagetype_pkey PRIMARY KEY (stage_type_pk)
);


-- public.base_team definition

-- Drop table

-- DROP TABLE public.base_team;

CREATE TABLE public.base_team (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	team_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	team_id int8 NOT NULL,
	team_name varchar(255) NOT NULL,
	team_acronym varchar(255) NOT NULL,
	team_slug varchar(255) NOT NULL,
	CONSTRAINT base_team_pkey PRIMARY KEY (team_pk),
	CONSTRAINT base_team_team_id_ece94006_uniq UNIQUE (team_id)
);
CREATE INDEX base_team_team_slug_91040475 ON public.base_team USING btree (team_slug);
CREATE INDEX base_team_team_slug_91040475_like ON public.base_team USING btree (team_slug varchar_pattern_ops);


-- public.base_tournament definition

-- Drop table

-- DROP TABLE public.base_tournament;

CREATE TABLE public.base_tournament (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	tournament_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	tournament_id int8 NOT NULL,
	tournament_name varchar(255) NOT NULL,
	tournament_slug varchar(255) NOT NULL,
	tournament_sport varchar(255) NOT NULL,
	tournament_start_date date NOT NULL,
	tournament_end_date date NOT NULL,
	CONSTRAINT base_tournament_pkey PRIMARY KEY (tournament_pk),
	CONSTRAINT base_tournament_tournament_id_7b383871_uniq UNIQUE (tournament_id)
);
CREATE INDEX base_tournament_tournament_slug_0ed805bf ON public.base_tournament USING btree (tournament_slug);
CREATE INDEX base_tournament_tournament_slug_0ed805bf_like ON public.base_tournament USING btree (tournament_slug varchar_pattern_ops);


-- public.django_content_type definition

-- Drop table

-- DROP TABLE public.django_content_type;

CREATE TABLE public.django_content_type (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model),
	CONSTRAINT django_content_type_pkey PRIMARY KEY (id)
);


-- public.django_migrations definition

-- Drop table

-- DROP TABLE public.django_migrations;

CREATE TABLE public.django_migrations (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
	app varchar(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	applied timestamptz NOT NULL,
	CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);


-- public.django_session definition

-- Drop table

-- DROP TABLE public.django_session;

CREATE TABLE public.django_session (
	session_key varchar(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamptz NOT NULL,
	CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


-- public.auth_permission definition

-- Drop table

-- DROP TABLE public.auth_permission;

CREATE TABLE public.auth_permission (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	"name" varchar(255) NOT NULL,
	content_type_id int4 NOT NULL,
	codename varchar(100) NOT NULL,
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
	CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
	CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


-- public.auth_user_groups definition

-- Drop table

-- DROP TABLE public.auth_user_groups;

CREATE TABLE public.auth_user_groups (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
	user_id int4 NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id),
	CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


-- public.auth_user_user_permissions definition

-- Drop table

-- DROP TABLE public.auth_user_user_permissions;

CREATE TABLE public.auth_user_user_permissions (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
	user_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
	CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


-- public.base_gamedetail definition

-- Drop table

-- DROP TABLE public.base_gamedetail;

CREATE TABLE public.base_gamedetail (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	game_detail_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	player_id int8 NOT NULL,
	game_detail_player_match bool NOT NULL,
	game_id int4 NOT NULL,
	CONSTRAINT base_gamedetail_pkey PRIMARY KEY (game_detail_pk),
	CONSTRAINT base_gamedetail_game_id_073de946_fk_base_game_game_pk FOREIGN KEY (game_id) REFERENCES public.base_game(game_pk) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX base_gamedetail_game_id_073de946 ON public.base_gamedetail USING btree (game_id);


-- public.base_stage definition

-- Drop table

-- DROP TABLE public.base_stage;

CREATE TABLE public.base_stage (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	stage_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	stage_name_id int4 NOT NULL,
	stage_type_id int4 NULL,
	stage_slug_id int4 NOT NULL,
	tournament_id int4 NULL,
	CONSTRAINT base_stage_pkey PRIMARY KEY (stage_pk),
	CONSTRAINT base_stage_stage_name_id_41b9eaaf_fk_base_stag FOREIGN KEY (stage_name_id) REFERENCES public.base_stagename(stage_name_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_stage_stage_slug_id_cac4541e_fk_base_stag FOREIGN KEY (stage_slug_id) REFERENCES public.base_stageslug(stage_slug_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_stage_stage_type_id_7b043bd3_fk_base_stag FOREIGN KEY (stage_type_id) REFERENCES public.base_stagetype(stage_type_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_stage_tournament_id_4dfc3685_fk_base_tour FOREIGN KEY (tournament_id) REFERENCES public.base_tournament(tournament_pk) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX base_stage_stage_name_id_41b9eaaf ON public.base_stage USING btree (stage_name_id);
CREATE INDEX base_stage_stage_slug_id_cac4541e ON public.base_stage USING btree (stage_slug_id);
CREATE INDEX base_stage_stage_type_id_7b043bd3 ON public.base_stage USING btree (stage_type_id);
CREATE INDEX base_stage_tournament_id_4dfc3685 ON public.base_stage USING btree (tournament_id);


-- public.django_admin_log definition

-- Drop table

-- DROP TABLE public.django_admin_log;

CREATE TABLE public.django_admin_log (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	action_time timestamptz NOT NULL,
	object_id text NULL,
	object_repr varchar(200) NOT NULL,
	action_flag int2 NOT NULL,
	change_message text NOT NULL,
	content_type_id int4 NULL,
	user_id int4 NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0)),
	CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
	CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


-- public.auth_group_permissions definition

-- Drop table

-- DROP TABLE public.auth_group_permissions;

CREATE TABLE public.auth_group_permissions (
	id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
	group_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
	CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


-- public.base_section definition

-- Drop table

-- DROP TABLE public.base_section;

CREATE TABLE public.base_section (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	section_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	section_name_id int4 NOT NULL,
	stage_pk int4 NOT NULL,
	CONSTRAINT base_section_pkey PRIMARY KEY (section_pk),
	CONSTRAINT base_section_section_name_id_7676e34f_fk_base_sect FOREIGN KEY (section_name_id) REFERENCES public.base_sectionname(section_name_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_section_stage_pk_b4c3015f_fk_base_stage_stage_pk FOREIGN KEY (stage_pk) REFERENCES public.base_stage(stage_pk) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX base_section_section_name_id_7676e34f ON public.base_section USING btree (section_name_id);
CREATE INDEX base_section_stage_pk_b4c3015f ON public.base_section USING btree (stage_pk);


-- public.base_match definition

-- Drop table

-- DROP TABLE public.base_match;

CREATE TABLE public.base_match (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_type_id int4 NOT NULL,
	match_state_id int4 NOT NULL,
	match_mode_id int4 NOT NULL,
	match_strategy_id int4 NOT NULL,
	section_pk int4 NOT NULL,
	CONSTRAINT base_match_pkey PRIMARY KEY (match_pk),
	CONSTRAINT base_match_match_mode_id_4a7b540e_fk_base_matc FOREIGN KEY (match_mode_id) REFERENCES public.base_matchmode(match_mode_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_match_match_state_id_0a4e636d_fk_base_matc FOREIGN KEY (match_state_id) REFERENCES public.base_matchstate(match_state_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_match_match_strategy_id_4f5554d4_fk_base_matc FOREIGN KEY (match_strategy_id) REFERENCES public.base_matchstrategy(match_strategy_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_match_match_type_id_7ef8aafa_fk_base_matc FOREIGN KEY (match_type_id) REFERENCES public.base_matchtype(match_type_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_match_section_pk_8802e1bb_fk_base_section_section_pk FOREIGN KEY (section_pk) REFERENCES public.base_section(section_pk) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX base_match_match_mode_id_4a7b540e ON public.base_match USING btree (match_mode_id);
CREATE INDEX base_match_match_state_id_0a4e636d ON public.base_match USING btree (match_state_id);
CREATE INDEX base_match_match_strategy_id_4f5554d4 ON public.base_match USING btree (match_strategy_id);
CREATE INDEX base_match_match_type_id_7ef8aafa ON public.base_match USING btree (match_type_id);
CREATE INDEX base_match_section_pk_8802e1bb ON public.base_match USING btree (section_pk);


-- public.base_matchdetail definition

-- Drop table

-- DROP TABLE public.base_matchdetail;

CREATE TABLE public.base_matchdetail (
	created_date timestamptz NOT NULL,
	modified_date timestamptz NOT NULL,
	match_detail_pk int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	match_detail_match_team_integrant bool NOT NULL,
	match_detail_win bool NOT NULL,
	match_id_id int4 NOT NULL,
	team_id_id int4 NOT NULL,
	CONSTRAINT base_matchdetail_pkey PRIMARY KEY (match_detail_pk),
	CONSTRAINT base_matchdetail_match_id_id_86c4ef38_fk_base_match_match_pk FOREIGN KEY (match_id_id) REFERENCES public.base_match(match_pk) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT base_matchdetail_team_id_id_a04671d9_fk_base_team_team_pk FOREIGN KEY (team_id_id) REFERENCES public.base_team(team_pk) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX base_matchdetail_match_id_id_86c4ef38 ON public.base_matchdetail USING btree (match_id_id);
CREATE INDEX base_matchdetail_team_id_id_a04671d9 ON public.base_matchdetail USING btree (team_id_id);