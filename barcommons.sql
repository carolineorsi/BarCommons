--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: questions; Type: TABLE; Schema: public; Owner: carolineorsi; Tablespace: 
--

CREATE TABLE questions (
    id integer NOT NULL,
    rule_id integer,
    question text,
    point_value integer,
    answer text
);


ALTER TABLE public.questions OWNER TO carolineorsi;

--
-- Name: rules; Type: TABLE; Schema: public; Owner: carolineorsi; Tablespace: 
--

CREATE TABLE rules (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.rules OWNER TO carolineorsi;

--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: carolineorsi
--

COPY questions (id, rule_id, question, point_value, answer) FROM stdin;
1	1	Where does Marco get to walk?	100	the beach
2	1	Who gets to walk on the beach in the morning?	50	Marco
3	2	How many ginger cookies does Janelle get to eat?	1000	all of them
4	2	What kind of cookies does Janelle get to eat?	250	ginger
\.


--
-- Data for Name: rules; Type: TABLE DATA; Schema: public; Owner: carolineorsi
--

COPY rules (id, name, description) FROM stdin;
1	Marco	Marco always gets to walk on the beach in the morning.
2	Janelle	Janelle gets to eat as many ginger cookies as she wants.
\.


--
-- Name: questions_pkey; Type: CONSTRAINT; Schema: public; Owner: carolineorsi; Tablespace: 
--

ALTER TABLE ONLY questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- Name: rules_pkey; Type: CONSTRAINT; Schema: public; Owner: carolineorsi; Tablespace: 
--

ALTER TABLE ONLY rules
    ADD CONSTRAINT rules_pkey PRIMARY KEY (id);


--
-- Name: questions_rule_if_fkey; Type: FK CONSTRAINT; Schema: public; Owner: carolineorsi
--

ALTER TABLE ONLY questions
    ADD CONSTRAINT questions_rule_if_fkey FOREIGN KEY (rule_id) REFERENCES rules(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: carolineorsi
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM carolineorsi;
GRANT ALL ON SCHEMA public TO carolineorsi;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

