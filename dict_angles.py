import math

slope_points = [(0, 157), (1, 157), (2, 157), (3, 157), (4, 157), (5, 157), (6, 157), (7, 157), (8, 157), (9, 157), (10, 157), (11, 157), (12, 157), (13, 157), (14, 157), (15, 157), (16, 157), (17, 157), (18, 157), (19, 157), (20, 157), (21, 157), (22, 158), (23, 158), (24, 158), (25, 158), (26, 159), (27, 159), (28, 159), (29, 159), (30, 160), (31, 160), (32, 160), (33, 160), (34, 161), (35, 161), (36, 162), (37, 162), (38, 162), (39, 163), (40, 163), (41, 164), (42, 164), (43, 164), (44, 165), (45, 165), (46, 166), (47, 167), (48, 167), (49, 168), (50, 168), (51, 169), (52, 169), (53, 170), (54, 171), (55, 171), (56, 172), (57, 172), (58, 173), (59, 173), (60, 174), (61, 175), (62, 175), (63, 176), (64, 176), (65, 177), (66, 178), (67, 179), (68, 179), (69, 180), (70, 181), (71, 182), (72, 183), (73, 183), (74, 184), (75, 185), (76, 186), (77, 186), (78, 187), (79, 188), (80, 189), (81, 189), (82, 190), (83, 191), (84, 192), (85, 193), (86, 194), (87, 195), (88, 195), (89, 196), (90, 197), (91, 198), (92, 199), (93, 200), (94, 201), (95, 202), (96, 203), (97, 204), (98, 204), (99, 205), (100, 206), (101, 207), (102, 208), (103, 209), (104, 210), (105, 211), (106, 212), (107, 213), (108, 213), (109, 214), (110, 215), (111, 216), (112, 217), (113, 218), (114, 219), (115, 220), (116, 221), (117, 222), (118, 223), (119, 224), (120, 224), (121, 225), (122, 226), (123, 227), (124, 228), (125, 229), (126, 230), (127, 231), (128, 232), (129, 232), (130, 233), (131, 234), (132, 235), (133, 236), (134, 237), (135, 237), (136, 238), (137, 239), (138, 240), (139, 241), (140, 241), (141, 242), (142, 243), (143, 244), (144, 245), (145, 245), (146, 246), (147, 247), (148, 248), (149, 248), (150, 249), (151, 250), (152, 250), (153, 251), (154, 252), (155, 252), (156, 253), (157, 254), (158, 254), (159, 255), (160, 256), (161, 256), (162, 257), (163, 257), (164, 258), (165, 259), (166, 259), (167, 260), (168, 260), (169, 261), (170, 261), (171, 262), (172, 262), (173, 263), (174, 263), (175, 263), (176, 264), (177, 264), (178, 265), (179, 265), (180, 265), (181, 266), (182, 266), (183, 267), (184, 267), (185, 267), (186, 267), (187, 268), (188, 268), (189, 268), (190, 269), (191, 269), (192, 269), (193, 269), (194, 269), (195, 270), (196, 270), (197, 270), (198, 270), (199, 270), (200, 270), (201, 270), (202, 270), (203, 271), (204, 271), (205, 271), (206, 271), (207, 271), (208, 271), (209, 271), (210, 271), (211, 271), (212, 271), (213, 271), (214, 270), (215, 270), (216, 270), (217, 270), (218, 270), (219, 270), (220, 270), (221, 270), (222, 269), (223, 269), (224, 269), (225, 269), (226, 268), (227, 268), (228, 268), (229, 268), (230, 267), (231, 267), (232, 267), (233, 267), (234, 266), (235, 266), (236, 265), (237, 265), (238, 265), (239, 264), (240, 264), (241, 264), (242, 263), (243, 263), (244, 262), (245, 262), (246, 261), (247, 261), (248, 260), (249, 260), (250, 259), (251, 259), (252, 258), (253, 258), (254, 257), (255, 257), (256, 256), (257, 256), (258, 255), (259, 255), (260, 254), (261, 254), (262, 253), (263, 252), (264, 252), (265, 251), (266, 251), (267, 250), (268, 249), (269, 249), (270, 248), (271, 248), (272, 247), (273, 246), (274, 246), (275, 245), (276, 244), (277, 244), (278, 243), (279, 242), (280, 242), (281, 241), (282, 240), (283, 240), (284, 239), (285, 238), (286, 238), (287, 237), (288, 236), (289, 236), (290, 235), (291, 234), (292, 234), (293, 233), (294, 232), (295, 232), (296, 231), (297, 230), (298, 230), (299, 229), (300, 228), (301, 228), (302, 227), (303, 226), (304, 226), (305, 225), (306, 224), (307, 224), (308, 223), (309, 223), (310, 222), (311, 221), (312, 221), (313, 220), (314, 220), (315, 219), (316, 218), (317, 218), (318, 217), (319, 217), (320, 216), (321, 215), (322, 215), (323, 214), (324, 214), (325, 213), (326, 213), (327, 212), (328, 212), (329, 211), (330, 211), (331, 211), (332, 210), (333, 210), (334, 209), (335, 209), (336, 209), (337, 208), (338, 208), (339, 207), (340, 207), (341, 207), (342, 206), (343, 206), (344, 206), (345, 205), (346, 205), (347, 205), (348, 205), (349, 204), (350, 204), (351, 204), (352, 204), (353, 204), (354, 203), (355, 203), (356, 203), (357, 203), (358, 203), (359, 203), (360, 203), (361, 203), (362, 203), (363, 203), (364, 203), (365, 203), (366, 203), (367, 204), (368, 204), (369, 204), (370, 204), (371, 205), (372, 205), (373, 205), (374, 205), (375, 205), (376, 206), (377, 206), (378, 207), (379, 207), (380, 208), (381, 208), (382, 209), (383, 209), (384, 210), (385, 210), (386, 211), (387, 211), (388, 212), (389, 213), (390, 214), (391, 214), (392, 215), (393, 216), (394, 217), (395, 218), (396, 219), (397, 219), (398, 221), (399, 222), (400, 223), (401, 224), (402, 225), (403, 227), (404, 228), (405, 229), (406, 230), (407, 232), (408, 233), (409, 235), (410, 237), (411, 238), (412, 240), (413, 241), (414, 243), (415, 245), (416, 246), (417, 248), (418, 249), (419, 251), (420, 253), (421, 254), (422, 256), (423, 257), (424, 259), (425, 261), (426, 262), (427, 264), (428, 265), (429, 266), (430, 268), (431, 269), (432, 270), (433, 271), (434, 273), (435, 274), (436, 275), (437, 276), (438, 277), (439, 278), (440, 279), (441, 280), (442, 280), (443, 281), (444, 282), (445, 282), (446, 283), (447, 284), (448, 284), (449, 285), (450, 285), (451, 286), (452, 286), (453, 286), (454, 287), (455, 287), (456, 287), (457, 287), (458, 288), (459, 288), (460, 288), (461, 288), (462, 288), (463, 288), (464, 288), (465, 288), (466, 288), (467, 288), (468, 288), (469, 288), (470, 288), (471, 288), (472, 287), (473, 287), (474, 287), (475, 287), (476, 286), (477, 286), (478, 286), (479, 285), (480, 285), (481, 284), (482, 284), (483, 283), (484, 283), (485, 282), (486, 282), (487, 281), (488, 281), (489, 280), (490, 280), (491, 279), (492, 278), (493, 278), (494, 277), (495, 276), (496, 276), (497, 275), (498, 274), (499, 274), (500, 273), (501, 272), (502, 271), (503, 271), (504, 270), (505, 269), (506, 269), (507, 268), (508, 267), (509, 266), (510, 266), (511, 265), (512, 264), (513, 264), (514, 263), (515, 262), (516, 262), (517, 261), (518, 260), (519, 260), (520, 259), (521, 258), (522, 258), (523, 257), (524, 256), (525, 256), (526, 256), (527, 255), (528, 255), (529, 254), (530, 254), (531, 253), (532, 253), (533, 252), (534, 252), (535, 252), (536, 252), (537, 251), (538, 251), (539, 251), (540, 251), (541, 250), (542, 250), (543, 250), (544, 250), (545, 250), (546, 250), (547, 250), (548, 250), (549, 250), (550, 250), (551, 250), (552, 250), (553, 250), (554, 250), (555, 250), (556, 250), (557, 250), (558, 251), (559, 251), (560, 251), (561, 251), (562, 251), (563, 252), (564, 252), (565, 252), (566, 252), (567, 253), (568, 253), (569, 253), (570, 254), (571, 254), (572, 254), (573, 255), (574, 255), (575, 255), (576, 256), (577, 256), (578, 257), (579, 257), (580, 257), (581, 258), (582, 258), (583, 259), (584, 259), (585, 260), (586, 260), (587, 261), (588, 261), (589, 262), (590, 262), (591, 262), (592, 263), (593, 263), (594, 264), (595, 264), (596, 265), (597, 265), (598, 266), (599, 266), (600, 267), (601, 267), (602, 268), (603, 268), (604, 269), (605, 269), (606, 270), (607, 270), (608, 271), (609, 271), (610, 272), (611, 272), (612, 273), (613, 273), (614, 274), (615, 274), (616, 275), (617, 276), (618, 276), (619, 277), (620, 277), (621, 278), (622, 278), (623, 279), (624, 279), (625, 280), (626, 281), (627, 281), (628, 282), (629, 282), (630, 283), (631, 283), (632, 284), (633, 284), (634, 285), (635, 286), (636, 286), (637, 287), (638, 287), (639, 288), (640, 288), (641, 289), (642, 289), (643, 290), (644, 291), (645, 291), (646, 292), (647, 292), (648, 293), (649, 293), (650, 294), (651, 295), (652, 295), (653, 296), (654, 296), (655, 297), (656, 297), (657, 298), (658, 299), (659, 299), (660, 300), (661, 300), (662, 301), (663, 302), (664, 302), (665, 303), (666, 303), (667, 304), (668, 305), (669, 305), (670, 306), (671, 306), (672, 307), (673, 308), (674, 308), (675, 309), (676, 309), (677, 310), (678, 311), (679, 311), (680, 312), (681, 312), (682, 313), (683, 314), (684, 314), (685, 315), (686, 315), (687, 316), (688, 316), (689, 317), (690, 318), (691, 318), (692, 319), (693, 319), (694, 320), (695, 321), (696, 321), (697, 322), (698, 322), (699, 323), (700, 324), (701, 324), (702, 325), (703, 325), (704, 326), (705, 326), (706, 327), (707, 327), (708, 328), (709, 329), (710, 329), (711, 330), (712, 330), (713, 331), (714, 331), (715, 332), (716, 332), (717, 333), (718, 334), (719, 334), (720, 335), (721, 335), (722, 336), (723, 336), (724, 337), (725, 337), (726, 338), (727, 338), (728, 339), (729, 339), (730, 340), (731, 340), (732, 341), (733, 341), (734, 342), (735, 342), (736, 343), (737, 343), (738, 344), (739, 344), (740, 345), (741, 345), (742, 346), (743, 346), (744, 347), (745, 347), (746, 348), (747, 348), (748, 349), (749, 349), (750, 350), (751, 350), (752, 350), (753, 351), (754, 351), (755, 352), (756, 352), (757, 353), (758, 353), (759, 353), (760, 354), (761, 354), (762, 355), (763, 355), (764, 355), (765, 356), (766, 356), (767, 357), (768, 357), (769, 357), (770, 358), (771, 358), (772, 358), (773, 359), (774, 359), (775, 359), (776, 360), (777, 360), (778, 360), (779, 361), (780, 361), (781, 361), (782, 362), (783, 362), (784, 362), (785, 363), (786, 363), (787, 363), (788, 364), (789, 364), (790, 364), (791, 364), (792, 365), (793, 365), (794, 365), (795, 365), (796, 366), (797, 366), (798, 366), (799, 367), (800, 367), (801, 367), (802, 367), (803, 367), (804, 368), (805, 368), (806, 368), (807, 368), (808, 369), (809, 369), (810, 369), (811, 369), (812, 369), (813, 369), (814, 370), (815, 370), (816, 370), (817, 370), (818, 370), (819, 371), (820, 371), (821, 371), (822, 371), (823, 371), (824, 371), (825, 371), (826, 372), (827, 372), (828, 372), (829, 372), (830, 372), (831, 372), (832, 372), (833, 372), (834, 372), (835, 372), (836, 373), (837, 373), (838, 373), (839, 373), (840, 373), (841, 373), (842, 373), (843, 373), (844, 373), (845, 373), (846, 373), (847, 373), (848, 373), (849, 373), (850, 373), (851, 373), (852, 373), (853, 373), (854, 373), (855, 373), (856, 373), (857, 373), (858, 373), (859, 373), (860, 373), (861, 373), (862, 373), (863, 373), (864, 373), (865, 373), (866, 373), (867, 373), (868, 373), (869, 372), (870, 372), (871, 372), (872, 372), (873, 372), (874, 372), (875, 372), (876, 372), (877, 372), (878, 371), (879, 371), (880, 371), (881, 371), (882, 371), (883, 371), (884, 370), (885, 370), (886, 370), (887, 370), (888, 370), (889, 369), (890, 369), (891, 369), (892, 369), (893, 369), (894, 368), (895, 368), (896, 368), (897, 367), (898, 367), (899, 367), (900, 367), (901, 366), (902, 366), (903, 366), (904, 365), (905, 365), (906, 365), (907, 364), (908, 364), (909, 364), (910, 363), (911, 363), (912, 362), (913, 362), (914, 361), (915, 361), (916, 361), (917, 360), (918, 360), (919, 359), (920, 359), (921, 358), (922, 358), (923, 357), (924, 357), (925, 356), (926, 356), (927, 355), (928, 355), (929, 354), (930, 353), (931, 353), (932, 352), (933, 351), (934, 351), (935, 350), (936, 349), (937, 349), (938, 348), (939, 347), (940, 347), (941, 346), (942, 345), (943, 344), (944, 344), (945, 343), (946, 342), (947, 341), (948, 340), (949, 339), (950, 338), (951, 337), (952, 336), (953, 336), (954, 335), (955, 334), (956, 333), (957, 332), (958, 331), (959, 330), (960, 329), (961, 328), (962, 327), (963, 326), (964, 325), (965, 324), (966, 324), (967, 323), (968, 322), (969, 321), (970, 320), (971, 319), (972, 318), (973, 318), (974, 317), (975, 316), (976, 315), (977, 315), (978, 314), (979, 313), (980, 312), (981, 312), (982, 311), (983, 311), (984, 310), (985, 310), (986, 309), (987, 309), (988, 308), (989, 308), (990, 307), (991, 307), (992, 306), (993, 306), (994, 305), (995, 305), (996, 305), (997, 305), (998, 304), (999, 304), (1000, 304), (1001, 304), (1002, 304), (1003, 303), (1004, 303), (1005, 303), (1006, 303), (1007, 303), (1008, 302), (1009, 303), (1010, 303), (1011, 303), (1012, 303), (1013, 303), (1014, 303), (1015, 303), (1016, 303), (1017, 303), (1018, 303), (1019, 303), (1020, 303), (1021, 303), (1022, 303), (1023, 303), (1024, 303), (1025, 303), (1026, 304), (1027, 304), (1028, 304), (1029, 304), (1030, 305), (1031, 305), (1032, 305), (1033, 305), (1034, 306), (1035, 306), (1036, 306), (1037, 307), (1038, 307), (1039, 307), (1040, 308), (1041, 308), (1042, 309), (1043, 309), (1044, 310), (1045, 310), (1046, 311), (1047, 311), (1048, 312), (1049, 312), (1050, 313), (1051, 313), (1052, 314), (1053, 314), (1054, 315), (1055, 316), (1056, 316), (1057, 317), (1058, 317), (1059, 318), (1060, 318), (1061, 319), (1062, 319), (1063, 320), (1064, 321), (1065, 321), (1066, 322), (1067, 323), (1068, 324), (1069, 324), (1070, 325), (1071, 326), (1072, 327), (1073, 327), (1074, 328), (1075, 329), (1076, 330), (1077, 330), (1078, 331), (1079, 332), (1080, 333), (1081, 333), (1082, 334), (1083, 335), (1084, 336), (1085, 337), (1086, 337), (1087, 338), (1088, 339), (1089, 340), (1090, 341), (1091, 342), (1092, 343), (1093, 343), (1094, 344), (1095, 345), (1096, 346), (1097, 347), (1098, 348), (1099, 349), (1100, 350), (1101, 350), (1102, 351), (1103, 352), (1104, 353), (1105, 354), (1106, 355), (1107, 356), (1108, 356), (1109, 357), (1110, 358), (1111, 359), (1112, 360), (1113, 360), (1114, 361), (1115, 362), (1116, 363), (1117, 363), (1118, 364), (1119, 365), (1120, 365), (1121, 366), (1122, 367), (1123, 367), (1124, 368), (1125, 369), (1126, 369), (1127, 370), (1128, 371), (1129, 371), (1130, 372), (1131, 373), (1132, 373), (1133, 374), (1134, 374), (1135, 375), (1136, 375), (1137, 376), (1138, 377), (1139, 377), (1140, 378), (1141, 378), (1142, 379), (1143, 379), (1144, 380), (1145, 380), (1146, 380), (1147, 381), (1148, 381), (1149, 382), (1150, 382), (1151, 383), (1152, 383), (1153, 383), (1154, 384), (1155, 384), (1156, 384), (1157, 385), (1158, 385), (1159, 385), (1160, 386), (1161, 386), (1162, 386), (1163, 386), (1164, 387), (1165, 387), (1166, 387), (1167, 387), (1168, 387), (1169, 387), (1170, 388), (1171, 388), (1172, 388), (1173, 388), (1174, 388), (1175, 388), (1176, 388), (1177, 388), (1178, 388), (1179, 388), (1180, 388), (1181, 388), (1182, 388), (1183, 388), (1184, 388), (1185, 388), (1186, 388), (1187, 387), (1188, 387), (1189, 387), (1190, 387), (1191, 387), (1192, 386), (1193, 386), (1194, 386), (1195, 385), (1196, 385), (1197, 385), (1198, 384), (1199, 384), (1200, 383), (1201, 383), (1202, 382), (1203, 382), (1204, 381), (1205, 381), (1206, 380), (1207, 379), (1208, 379), (1209, 378), (1210, 377), (1211, 376), (1212, 376), (1213, 375), (1214, 374), (1215, 373), (1216, 372), (1217, 371), (1218, 370), (1219, 369), (1220, 369), (1221, 368), (1222, 367), (1223, 366), (1224, 365), (1225, 364), (1226, 363), (1227, 363), (1228, 362), (1229, 361), (1230, 360), (1231, 359), (1232, 359), (1233, 358), (1234, 358), (1235, 357), (1236, 356), (1237, 356), (1238, 355), (1239, 355), (1240, 355), (1241, 354), (1242, 354), (1243, 354), (1244, 354), (1245, 353), (1246, 353), (1247, 353), (1248, 353), (1249, 353), (1250, 353), (1251, 353), (1252, 353), (1253, 353), (1254, 353), (1255, 353), (1256, 353), (1257, 354), (1258, 354), (1259, 354), (1260, 354), (1261, 355), (1262, 355), (1263, 356), (1264, 356), (1265, 357), (1266, 357), (1267, 358), (1268, 358), (1269, 359), (1270, 360), (1271, 360), (1272, 361), (1273, 361), (1274, 362), (1275, 363), (1276, 364), (1277, 365), (1278, 366), (1279, 366), (1280, 367), (1281, 368), (1282, 369), (1283, 370), (1284, 371), (1285, 371), (1286, 372), (1287, 373), (1288, 374), (1289, 375), (1290, 376), (1291, 377), (1292, 377), (1293, 378), (1294, 379), (1295, 380), (1296, 381), (1297, 381), (1298, 382), (1299, 383), (1300, 383), (1301, 384), (1302, 385), (1303, 385), (1304, 386), (1305, 386), (1306, 387), (1307, 387), (1308, 388), (1309, 388), (1310, 388), (1311, 389), (1312, 389), (1313, 389), (1314, 390), (1315, 390), (1316, 390), (1317, 390), (1318, 390), (1319, 390), (1320, 391), (1321, 391), (1322, 391), (1323, 391), (1324, 391), (1325, 391), (1326, 391), (1327, 391), (1328, 391), (1329, 391), (1330, 391), (1331, 391), (1332, 391), (1333, 390), (1334, 390), (1335, 390), (1336, 390), (1337, 390), (1338, 390), (1339, 389), (1340, 389), (1341, 389), (1342, 389), (1343, 388), (1344, 388), (1345, 388), (1346, 388), (1347, 387), (1348, 387), (1349, 387), (1350, 387), (1351, 386), (1352, 386), (1353, 386), (1354, 385), (1355, 385), (1356, 385), (1357, 384), (1358, 384), (1359, 384), (1360, 383), (1361, 383), (1362, 382), (1363, 382), (1364, 382), (1365, 381), (1366, 381), (1367, 381), (1368, 380), (1369, 380), (1370, 380), (1371, 379), (1372, 379), (1373, 379), (1374, 378), (1375, 378), (1376, 378), (1377, 377), (1378, 377), (1379, 377), (1380, 376), (1381, 376), (1382, 376), (1383, 375), (1384, 375), (1385, 375), (1386, 374), (1387, 374), (1388, 374), (1389, 373), (1390, 373), (1391, 373), (1392, 372), (1393, 372), (1394, 372), (1395, 372), (1396, 371), (1397, 371), (1398, 371), (1399, 371), (1400, 371), (1401, 371), (1402, 370), (1403, 370), (1404, 370), (1405, 370), (1406, 370), (1407, 370), (1408, 370), (1409, 369), (1410, 369), (1411, 369), (1412, 370), (1413, 370), (1414, 370), (1415, 370), (1416, 370), (1417, 370), (1418, 370), (1419, 370), (1420, 370), (1421, 370), (1422, 370), (1423, 370), (1424, 371), (1425, 371), (1426, 371), (1427, 371), (1428, 372), (1429, 372), (1430, 372), (1431, 373), (1432, 373), (1433, 373), (1434, 374), (1435, 374), (1436, 374), (1437, 375), (1438, 376), (1439, 376), (1440, 377), (1441, 377), (1442, 378), (1443, 379), (1444, 379), (1445, 380), (1446, 381), (1447, 381), (1448, 382), (1449, 383), (1450, 384), (1451, 385), (1452, 386), (1453, 387), (1454, 388), (1455, 388), (1456, 390), (1457, 391), (1458, 392), (1459, 393), (1460, 394), (1461, 395), (1462, 396), (1463, 397), (1464, 398), (1465, 400), (1466, 401), (1467, 402), (1468, 404), (1469, 405), (1470, 406), (1471, 408), (1472, 409), (1473, 410), (1474, 412), (1475, 413), (1476, 414), (1477, 416), (1478, 417), (1479, 419), (1480, 420), (1481, 421), (1482, 423), (1483, 424), (1484, 426), (1485, 427), (1486, 428), (1487, 430), (1488, 431), (1489, 433), (1490, 434), (1491, 435), (1492, 437), (1493, 438), (1494, 439), (1495, 441), (1496, 442), (1497, 443), (1498, 445), (1499, 446), (1500, 447), (1501, 449), (1502, 450), (1503, 451), (1504, 452), (1505, 453), (1506, 455), (1507, 456), (1508, 457), (1509, 458), (1510, 459), (1511, 461), (1512, 462), (1513, 463), (1514, 464), (1515, 465), (1516, 466), (1517, 467), (1518, 468), (1519, 469), (1520, 470), (1521, 471), (1522, 472), (1523, 473), (1524, 474), (1525, 475), (1526, 476), (1527, 477), (1528, 478), (1529, 479), (1530, 480), (1531, 481), (1532, 482), (1533, 483), (1534, 483), (1535, 484), (1536, 485), (1537, 486), (1538, 487), (1539, 487), (1540, 488), (1541, 489), (1542, 490), (1543, 490), (1544, 491), (1545, 492), (1546, 492), (1547, 493), (1548, 494), (1549, 494), (1550, 495), (1551, 496), (1552, 496), (1553, 497), (1554, 497), (1555, 498), (1556, 499), (1557, 499), (1558, 500), (1559, 500), (1560, 501), (1561, 501), (1562, 502), (1563, 502), (1564, 502), (1565, 503), (1566, 503), (1567, 504), (1568, 504), (1569, 505), (1570, 505), (1571, 505), (1572, 506), (1573, 506), (1574, 506), (1575, 507), (1576, 507), (1577, 507), (1578, 508), (1579, 508), (1580, 508), (1581, 508), (1582, 509), (1583, 509), (1584, 509), (1585, 509), (1586, 510), (1587, 510), (1588, 510), (1589, 510), (1590, 510), (1591, 511), (1592, 511), (1593, 511), (1594, 511), (1595, 511), (1596, 511), (1597, 511), (1598, 511), (1599, 512), (1600, 512), (1601, 512), (1602, 512), (1603, 512), (1604, 512), (1605, 512), (1606, 512), (1607, 512), (1608, 512), (1609, 512), (1610, 512), (1611, 512), (1612, 512), (1613, 512), (1614, 511), (1615, 511), (1616, 511), (1617, 511), (1618, 511), (1619, 511), (1620, 511), (1621, 511), (1622, 510), (1623, 510), (1624, 510), (1625, 510), (1626, 510), (1627, 509), (1628, 509), (1629, 509), (1630, 508), (1631, 508), (1632, 508), (1633, 507), (1634, 507), (1635, 507), (1636, 506), (1637, 506), (1638, 505), (1639, 505), (1640, 505), (1641, 504), (1642, 504), (1643, 503), (1644, 502), (1645, 502), (1646, 501), (1647, 501), (1648, 500), (1649, 499), (1650, 499), (1651, 498), (1652, 497), (1653, 496), (1654, 495), (1655, 495), (1656, 494), (1657, 493), (1658, 492), (1659, 491), (1660, 490), (1661, 489), (1662, 488), (1663, 487), (1664, 485), (1665, 484), (1666, 483), (1667, 482), (1668, 481), (1669, 479), (1670, 478), (1671, 477), (1672, 475), (1673, 474), (1674, 472), (1675, 471), (1676, 470), (1677, 468), (1678, 467), (1679, 465), (1680, 464), (1681, 462), (1682, 461), (1683, 460), (1684, 458), (1685, 457), (1686, 455), (1687, 454), (1688, 452), (1689, 451), (1690, 450), (1691, 448), (1692, 447), (1693, 446), (1694, 445), (1695, 443), (1696, 442), (1697, 441), (1698, 440), (1699, 439), (1700, 438), (1701, 437), (1702, 436), (1703, 435), (1704, 434), (1705, 433), (1706, 432), (1707, 432), (1708, 431), (1709, 430), (1710, 430), (1711, 429), (1712, 428), (1713, 428), (1714, 427), (1715, 427), (1716, 426), (1717, 425), (1718, 425), (1719, 425), (1720, 424), (1721, 424), (1722, 424), (1723, 424), (1724, 423), (1725, 423), (1726, 423), (1727, 423), (1728, 422), (1729, 422), (1730, 422), (1731, 422), (1732, 422), (1733, 422), (1734, 422), (1735, 422), (1736, 422), (1737, 422), (1738, 422), (1739, 422), (1740, 422), (1741, 422), (1742, 423), (1743, 423), (1744, 423), (1745, 423), (1746, 423), (1747, 424), (1748, 424), (1749, 424), (1750, 425), (1751, 425), (1752, 426), (1753, 426), (1754, 426), (1755, 427), (1756, 427), (1757, 428), (1758, 428), (1759, 429), (1760, 430), (1761, 430), (1762, 431), (1763, 432), (1764, 432), (1765, 433), (1766, 434), (1767, 435), (1768, 436), (1769, 437), (1770, 437), (1771, 438), (1772, 439), (1773, 440), (1774, 441), (1775, 442), (1776, 443), (1777, 444), (1778, 445), (1779, 446), (1780, 447), (1781, 448), (1782, 449), (1783, 451), (1784, 452), (1785, 453), (1786, 454), (1787, 455), (1788, 457), (1789, 458), (1790, 459), (1791, 460), (1792, 462), (1793, 463), (1794, 464), (1795, 466), (1796, 467), (1797, 468), (1798, 469), (1799, 471), (1800, 472), (1801, 473), (1802, 474), (1803, 476), (1804, 477), (1805, 478), (1806, 479), (1807, 480), (1808, 481), (1809, 482), (1810, 483), (1811, 484), (1812, 485), (1813, 486), (1814, 487), (1815, 488), (1816, 489), (1817, 490), (1818, 491), (1819, 491), (1820, 492), (1821, 493), (1822, 494), (1823, 494), (1824, 495), (1825, 496), (1826, 497), (1827, 497), (1828, 498), (1829, 498), (1830, 499), (1831, 500), (1832, 500), (1833, 501), (1834, 501), (1835, 502), (1836, 502), (1837, 503), (1838, 503), (1839, 503), (1840, 504), (1841, 504), (1842, 505), (1843, 505), (1844, 505), (1845, 505), (1846, 506), (1847, 506), (1848, 506), (1849, 506), (1850, 507), (1851, 507), (1852, 507), (1853, 507), (1854, 507), (1855, 507), (1856, 507), (1857, 507), (1858, 507), (1859, 507), (1860, 507), (1861, 507), (1862, 506), (1863, 506), (1864, 506), (1865, 506), (1866, 505), (1867, 505), (1868, 505), (1869, 504), (1870, 504), (1871, 503), (1872, 503), (1873, 502), (1874, 501), (1875, 501), (1876, 500), (1877, 499), (1878, 498), (1879, 497), (1880, 496), (1881, 495), (1882, 494), (1883, 493), (1884, 492), (1885, 491), (1886, 490), (1887, 489), (1888, 488), (1889, 487), (1890, 486), (1891, 485), (1892, 484), (1893, 483), (1894, 482), (1895, 481), (1896, 481), (1897, 480), (1898, 479), (1899, 479), (1900, 478), (1901, 478), (1902, 478), (1903, 478), (1904, 477), (1905, 477), (1906, 477), (1907, 477), (1908, 477), (1909, 477), (1910, 477), (1911, 477), (1912, 478), (1913, 478), (1914, 478), (1915, 479), (1916, 479), (1917, 480), (1918, 481), (1919, 482), (1920, 483), (1921, 484), (1922, 485), (1923, 486), (1924, 487), (1925, 488), (1926, 489), (1927, 490), (1928, 492), (1929, 493), (1930, 494), (1931, 496), (1932, 497), (1933, 498), (1934, 499), (1935, 500), (1936, 501), (1937, 502), (1938, 503), (1939, 504), (1940, 504), (1941, 505), (1942, 506), (1943, 506), (1944, 506), (1945, 507), (1946, 507), (1947, 508), (1948, 508), (1949, 508), (1950, 508), (1951, 509), (1952, 509), (1953, 509), (1954, 509), (1955, 509), (1956, 509), (1957, 509), (1958, 509), (1959, 509), (1960, 509), (1961, 509), (1962, 509), (1963, 508), (1964, 508), (1965, 508), (1966, 508), (1967, 508), (1968, 508), (1969, 508), (1970, 507), (1971, 507), (1972, 507), (1973, 507), (1974, 506), (1975, 506), (1976, 506), (1977, 506), (1978, 505), (1979, 505), (1980, 505), (1981, 505), (1982, 504), (1983, 504), (1984, 504), (1985, 504), (1986, 503), (1987, 503), (1988, 503), (1989, 503), (1990, 502), (1991, 502), (1992, 502), (1993, 502), (1994, 501), (1995, 501), (1996, 501), (1997, 501), (1998, 500), (1999, 500), (2000, 500), (2001, 500), (2002, 499), (2003, 499), (2004, 499), (2005, 499), (2006, 499), (2007, 499), (2008, 499), (2009, 499), (2010, 499), (2011, 499), (2012, 499), (2013, 499), (2014, 499), (2015, 499), (2016, 499), (2017, 499), (2018, 499), (2019, 499), (2020, 499), (2021, 499), (2022, 499), (2023, 499), (2024, 500), (2025, 500), (2026, 500), (2027, 500), (2028, 501), (2029, 501), (2030, 501), (2031, 502), (2032, 502), (2033, 502), (2034, 503), (2035, 503), (2036, 503), (2037, 504), (2038, 504), (2039, 504), (2040, 505), (2041, 505), (2042, 505), (2043, 506), (2044, 506), (2045, 507), (2046, 507), (2047, 508), (2048, 509), (2049, 509), (2050, 510), (2051, 510), (2052, 511), (2053, 512), (2054, 512), (2055, 513), (2056, 514), (2057, 514), (2058, 515), (2059, 516), (2060, 517), (2061, 518), (2062, 518), (2063, 519), (2064, 520), (2065, 521), (2066, 522), (2067, 523), (2068, 524), (2069, 525), (2070, 526), (2071, 527), (2072, 528), (2073, 528), (2074, 529), (2075, 530), (2076, 531), (2077, 532), (2078, 533), (2079, 534), (2080, 536), (2081, 537), (2082, 538), (2083, 539), (2084, 540), (2085, 541), (2086, 542), (2087, 543), (2088, 544), (2089, 546), (2090, 547), (2091, 548), (2092, 549), (2093, 550), (2094, 551), (2095, 553), (2096, 554), (2097, 555), (2098, 556), (2099, 557), (2100, 559), (2101, 560), (2102, 561), (2103, 562), (2104, 564), (2105, 565), (2106, 566), (2107, 567), (2108, 568), (2109, 570), (2110, 571), (2111, 572), (2112, 573), (2113, 575), (2114, 576), (2115, 577), (2116, 578), (2117, 579), (2118, 581), (2119, 582), (2120, 583), (2121, 584), (2122, 585), (2123, 586), (2124, 588), (2125, 589), (2126, 590), (2127, 591), (2128, 592), (2129, 593), (2130, 594), (2131, 595), (2132, 596), (2133, 597), (2134, 599), (2135, 599), (2136, 601), (2137, 602), (2138, 603), (2139, 604), (2140, 604), (2141, 605), (2142, 606), (2143, 607), (2144, 608), (2145, 609), (2146, 610), (2147, 611), (2148, 612), (2149, 613), (2150, 613), (2151, 614), (2152, 615), (2153, 616), (2154, 617), (2155, 617), (2156, 618), (2157, 619), (2158, 619), (2159, 620), (2160, 621), (2161, 622), (2162, 622), (2163, 623), (2164, 623), (2165, 624), (2166, 625), (2167, 625), (2168, 626), (2169, 626), (2170, 627), (2171, 627), (2172, 628), (2173, 628), (2174, 629), (2175, 629), (2176, 629), (2177, 630), (2178, 630), (2179, 631), (2180, 631), (2181, 631), (2182, 632), (2183, 632), (2184, 632), (2185, 633), (2186, 633), (2187, 633), (2188, 633), (2189, 633), (2190, 634), (2191, 634), (2192, 634), (2193, 634), (2194, 634), (2195, 634), (2196, 635), (2197, 635), (2198, 635), (2199, 635), (2200, 635), (2201, 635), (2202, 635), (2203, 635), (2204, 635), (2205, 635), (2206, 635), (2207, 635), (2208, 635), (2209, 635), (2210, 635), (2211, 635), (2212, 634), (2213, 634), (2214, 634), (2215, 634), (2216, 634), (2217, 634), (2218, 634), (2219, 633), (2220, 633), (2221, 633), (2222, 633), (2223, 632), (2224, 632), (2225, 632), (2226, 631), (2227, 631), (2228, 631), (2229, 630), (2230, 630), (2231, 630), (2232, 629), (2233, 629), (2234, 628), (2235, 628), (2236, 628), (2237, 627), (2238, 627), (2239, 626), (2240, 626), (2241, 625), (2242, 625), (2243, 624), (2244, 624), (2245, 623), (2246, 622), (2247, 622), (2248, 621), (2249, 621), (2250, 620), (2251, 620), (2252, 619), (2253, 618), (2254, 618), (2255, 617), (2256, 616), (2257, 616), (2258, 615), (2259, 614), (2260, 614), (2261, 613), (2262, 612), (2263, 611), (2264, 611), (2265, 610), (2266, 609), (2267, 608), (2268, 608), (2269, 607), (2270, 606), (2271, 605), (2272, 605), (2273, 604), (2274, 603), (2275, 602), (2276, 601), (2277, 601), (2278, 600), (2279, 599), (2280, 598), (2281, 597), (2282, 597), (2283, 596), (2284, 595), (2285, 594), (2286, 593), (2287, 592), (2288, 592), (2289, 591), (2290, 590), (2291, 589), (2292, 588), (2293, 588), (2294, 587), (2295, 586), (2296, 585), (2297, 585), (2298, 584), (2299, 583), (2300, 582), (2301, 582), (2302, 581), (2303, 580), (2304, 579), (2305, 579), (2306, 578), (2307, 577), (2308, 576), (2309, 576), (2310, 575), (2311, 574), (2312, 573), (2313, 573), (2314, 572), (2315, 571), (2316, 570), (2317, 570), (2318, 569), (2319, 569), (2320, 568), (2321, 567), (2322, 567), (2323, 566), (2324, 565), (2325, 565), (2326, 564), (2327, 564), (2328, 563), (2329, 562), (2330, 562), (2331, 562), (2332, 561), (2333, 561), (2334, 560), (2335, 560), (2336, 559), (2337, 559), (2338, 558), (2339, 558), (2340, 557), (2341, 557), (2342, 556), (2343, 556), (2344, 556), (2345, 555), (2346, 555), (2347, 555), (2348, 555), (2349, 554), (2350, 554), (2351, 554), (2352, 554), (2353, 553), (2354, 553), (2355, 553), (2356, 552), (2357, 552), (2358, 552), (2359, 552), (2360, 551), (2361, 551), (2362, 551), (2363, 550), (2364, 550), (2365, 550), (2366, 550), (2367, 550), (2368, 550), (2369, 550), (2370, 550), (2371, 550), (2372, 550), (2373, 550), (2374, 550), (2375, 550), (2376, 550), (2377, 549), (2378, 549), (2379, 549), (2380, 549), (2381, 549), (2382, 549), (2383, 549), (2384, 549), (2385, 549), (2386, 549), (2387, 549), (2388, 549), (2389, 549), (2390, 549), (2391, 550), (2392, 550), (2393, 550), (2394, 550), (2395, 550), (2396, 550), (2397, 550), (2398, 550), (2399, 550), (2400, 550), (2401, 551), (2402, 551), (2403, 551), (2404, 551), (2405, 551), (2406, 551), (2407, 551), (2408, 552), (2409, 552), (2410, 552), (2411, 552), (2412, 553), (2413, 553), (2414, 553), (2415, 554), (2416, 554), (2417, 554), (2418, 554), (2419, 555), (2420, 555), (2421, 555), (2422, 555), (2423, 556), (2424, 556), (2425, 556), (2426, 556), (2427, 557), (2428, 557), (2429, 558), (2430, 558), (2431, 558), (2432, 559), (2433, 559), (2434, 560), (2435, 560), (2436, 560), (2437, 561), (2438, 561), (2439, 561), (2440, 562), (2441, 562), (2442, 563), (2443, 563), (2444, 563), (2445, 564), (2446, 564), (2447, 565), (2448, 565), (2449, 566), (2450, 566), (2451, 567), (2452, 567), (2453, 568), (2454, 568), (2455, 569), (2456, 569), (2457, 570), (2458, 570), (2459, 571), (2460, 571), (2461, 572), (2462, 572), (2463, 573), (2464, 573), (2465, 574), (2466, 574), (2467, 575), (2468, 575), (2469, 576), (2470, 577), (2471, 577), (2472, 578), (2473, 578), (2474, 579), (2475, 580), (2476, 580), (2477, 581), (2478, 581), (2479, 582), (2480, 583), (2481, 583), (2482, 584), (2483, 584), (2484, 585), (2485, 586), (2486, 586), (2487, 587), (2488, 588), (2489, 588), (2490, 589), (2491, 590), (2492, 590), (2493, 591), (2494, 592), (2495, 592), (2496, 593), (2497, 594), (2498, 594), (2499, 595), (2500, 596), (2501, 596), (2502, 597), (2503, 598), (2504, 599), (2505, 599), (2506, 600), (2507, 601), (2508, 602), (2509, 602), (2510, 603), (2511, 604), (2512, 605), (2513, 605), (2514, 606), (2515, 607), (2516, 608), (2517, 608), (2518, 609), (2519, 610), (2520, 611), (2521, 611), (2522, 612), (2523, 613), (2524, 614), (2525, 614), (2526, 615), (2527, 616), (2528, 617), (2529, 617), (2530, 618), (2531, 619), (2532, 620), (2533, 620), (2534, 621), (2535, 622), (2536, 623), (2537, 623), (2538, 624), (2539, 625), (2540, 626), (2541, 627), (2542, 627), (2543, 628), (2544, 629), (2545, 630), (2546, 630), (2547, 631), (2548, 632), (2549, 633), (2550, 633), (2551, 634), (2552, 635), (2553, 636), (2554, 636), (2555, 637), (2556, 638), (2557, 639), (2558, 639), (2559, 640), (2560, 641), (2561, 641), (2562, 642), (2563, 643), (2564, 644), (2565, 644), (2566, 645), (2567, 646), (2568, 646), (2569, 647), (2570, 648), (2571, 648), (2572, 649), (2573, 650), (2574, 650), (2575, 651), (2576, 652), (2577, 652), (2578, 653), (2579, 654), (2580, 654), (2581, 655), (2582, 655), (2583, 656), (2584, 657), (2585, 657), (2586, 658), (2587, 658), (2588, 659), (2589, 660), (2590, 660), (2591, 661), (2592, 661), (2593, 662), (2594, 663), (2595, 663), (2596, 664), (2597, 664), (2598, 665), (2599, 665), (2600, 666), (2601, 666), (2602, 667), (2603, 668), (2604, 668), (2605, 669), (2606, 669), (2607, 670), (2608, 670), (2609, 671), (2610, 671), (2611, 672), (2612, 672), (2613, 672), (2614, 673), (2615, 673), (2616, 674), (2617, 674), (2618, 675), (2619, 675), (2620, 676), (2621, 676), (2622, 677), (2623, 677), (2624, 677), (2625, 678), (2626, 678), (2627, 679), (2628, 679), (2629, 679), (2630, 680), (2631, 680), (2632, 681), (2633, 681), (2634, 681), (2635, 682), (2636, 682), (2637, 682), (2638, 683), (2639, 683), (2640, 683), (2641, 684), (2642, 684), (2643, 684), (2644, 685), (2645, 685), (2646, 685), (2647, 686), (2648, 686), (2649, 686), (2650, 686), (2651, 687), (2652, 687), (2653, 687), (2654, 687), (2655, 688), (2656, 688), (2657, 688), (2658, 688), (2659, 688), (2660, 689), (2661, 689), (2662, 689), (2663, 689), (2664, 689), (2665, 690), (2666, 690), (2667, 690), (2668, 690), (2669, 690), (2670, 690), (2671, 690), (2672, 690), (2673, 691), (2674, 691), (2675, 691), (2676, 691), (2677, 691), (2678, 691), (2679, 691), (2680, 691), (2681, 691), (2682, 691), (2683, 691), (2684, 691), (2685, 691), (2686, 691), (2687, 691), (2688, 691), (2689, 691), (2690, 691), (2691, 691), (2692, 691), (2693, 691), (2694, 691), (2695, 691), (2696, 691), (2697, 691), (2698, 690), (2699, 690), (2700, 690), (2701, 690), (2702, 690), (2703, 690), (2704, 690), (2705, 689), (2706, 689), (2707, 689), (2708, 689), (2709, 689), (2710, 688), (2711, 688), (2712, 688), (2713, 688), (2714, 687), (2715, 687), (2716, 687), (2717, 686), (2718, 686), (2719, 686), (2720, 685), (2721, 685), (2722, 685), (2723, 684), (2724, 684), (2725, 683), (2726, 683), (2727, 682), (2728, 682), (2729, 681), (2730, 681), (2731, 680), (2732, 680), (2733, 679), (2734, 679), (2735, 678), (2736, 678), (2737, 677), (2738, 677), (2739, 676), (2740, 675), (2741, 675), (2742, 674), (2743, 673), (2744, 672), (2745, 672), (2746, 671), (2747, 670), (2748, 670), (2749, 669), (2750, 668), (2751, 667), (2752, 666), (2753, 666), (2754, 665), (2755, 664), (2756, 663), (2757, 662), (2758, 661), (2759, 661), (2760, 660), (2761, 659), (2762, 658), (2763, 657), (2764, 656), (2765, 656), (2766, 655), (2767, 654), (2768, 653), (2769, 652), (2770, 651), (2771, 651), (2772, 650), (2773, 649), (2774, 648), (2775, 648), (2776, 647), (2777, 646), (2778, 646), (2779, 645), (2780, 644), (2781, 644), (2782, 643), (2783, 642), (2784, 642), (2785, 641), (2786, 640), (2787, 640), (2788, 639), (2789, 639), (2790, 638), (2791, 638), (2792, 637), (2793, 637), (2794, 636), (2795, 636), (2796, 635), (2797, 635), (2798, 635), (2799, 634), (2800, 634), (2801, 633), (2802, 633), (2803, 633), (2804, 632), (2805, 632), (2806, 632), (2807, 631), (2808, 631), (2809, 631), (2810, 631), (2811, 630), (2812, 630), (2813, 630), (2814, 629), (2815, 629), (2816, 629), (2817, 629), (2818, 629), (2819, 629), (2820, 628), (2821, 628), (2822, 628), (2823, 628), (2824, 628), (2825, 628), (2826, 627), (2827, 627), (2828, 627), (2829, 627), (2830, 627), (2831, 627), (2832, 627), (2833, 627), (2834, 627), (2835, 627), (2836, 627), (2837, 627), (2838, 627), (2839, 627), (2840, 627), (2841, 627), (2842, 627), (2843, 627), (2844, 627), (2845, 627), (2846, 626), (2847, 626), (2848, 626), (2849, 626), (2850, 626), (2851, 626), (2852, 626), (2853, 626), (2854, 626), (2855, 626), (2856, 626), (2857, 626), (2858, 626), (2859, 626), (2860, 626), (2861, 626), (2862, 626), (2863, 626), (2864, 626), (2865, 626), (2866, 627), (2867, 627), (2868, 627), (2869, 627), (2870, 627), (2871, 627), (2872, 627), (2873, 627), (2874, 627), (2875, 627), (2876, 627), (2877, 627), (2878, 627), (2879, 627), (2880, 627), (2881, 628), (2882, 628), (2883, 628), (2884, 628), (2885, 628), (2886, 628), (2887, 628), (2888, 628), (2889, 628), (2890, 628), (2891, 628), (2892, 628), (2893, 628), (2894, 628), (2895, 628), (2896, 629), (2897, 629), (2898, 629), (2899, 629), (2900, 629), (2901, 629), (2902, 629), (2903, 629), (2904, 629), (2905, 629), (2906, 629), (2907, 629), (2908, 629), (2909, 629), (2910, 630), (2911, 630), (2912, 630), (2913, 630), (2914, 630), (2915, 630), (2916, 630), (2917, 630), (2918, 630), (2919, 630), (2920, 630), (2921, 630), (2922, 630), (2923, 630), (2924, 630), (2925, 630), (2926, 630), (2927, 630), (2928, 630), (2929, 630), (2930, 630), (2931, 630), (2932, 630), (2933, 630), (2934, 630), (2935, 630), (2936, 630), (2937, 630), (2938, 630), (2939, 630), (2940, 630), (2941, 630), (2942, 629), (2943, 629), (2944, 629), (2945, 629), (2946, 629), (2947, 629), (2948, 629), (2949, 629), (2950, 629), (2951, 628), (2952, 628), (2953, 628), (2954, 628), (2955, 628), (2956, 628), (2957, 627), (2958, 627), (2959, 627), (2960, 627), (2961, 627), (2962, 626), (2963, 626), (2964, 626), (2965, 626), (2966, 625), (2967, 625), (2968, 625), (2969, 625), (2970, 624), (2971, 624), (2972, 624), (2973, 623), (2974, 623), (2975, 623), (2976, 622), (2977, 622), (2978, 622), (2979, 621), (2980, 621), (2981, 621), (2982, 620), (2983, 620), (2984, 619), (2985, 619), (2986, 619), (2987, 618), (2988, 618), (2989, 617), (2990, 617), (2991, 616), (2992, 616), (2993, 615), (2994, 615), (2995, 614), (2996, 614), (2997, 613), (2998, 612), (2999, 612), (3000, 611), (3001, 611), (3002, 610), (3003, 609), (3004, 608), (3005, 608), (3006, 607), (3007, 606), (3008, 605), (3009, 604), (3010, 603), (3011, 602), (3012, 601), (3013, 600), (3014, 599), (3015, 598), (3016, 597), (3017, 596), (3018, 595), (3019, 593), (3020, 592), (3021, 590), (3022, 589), (3023, 587), (3024, 585), (3025, 583), (3026, 580), (3027, 577)]
p_dict = {x:[y] for x,y in slope_points}

for i in range(len(p_dict)):
    if i == 0:
        p_dict[i].append(0)
    elif i == len(p_dict)-1:
        p_dict[i].append(0)
    else:
        x1 = i-1
        x2 = i+1
        y1 = p_dict[i-1][0]
        y2 = p_dict[i+1][0]
        p_dict[i].append(math.atan2(x2-x1, y2-y1)-math.pi/2)


print p_dict