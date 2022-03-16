import 'package:animated_splash_screen/animated_splash_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import '../home.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  Widget build(BuildContext context) {
    return AnimatedSplashScreen(
      splash: SvgPicture.asset("assets/fruit.svg"),

      backgroundColor: const Color(0xFF0083B0),
      duration: 3000,
      splashIconSize: 300,
      nextScreen: const HomeScreen(),
      splashTransition: SplashTransition.rotationTransition,
      //pageTransitionType: PageTransitionType.scale,
      curve: Curves.easeInCirc,
    );
  }
}
