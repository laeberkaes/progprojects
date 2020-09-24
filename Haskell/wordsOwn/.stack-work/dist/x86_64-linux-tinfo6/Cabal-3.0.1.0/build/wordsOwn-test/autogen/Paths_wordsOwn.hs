{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_wordsOwn (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/bin"
libdir     = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/lib/x86_64-linux-ghc-8.8.4/wordsOwn-0.1.0.0-9fLXNlzqfTA1gsGgby6Q76-wordsOwn-test"
dynlibdir  = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/lib/x86_64-linux-ghc-8.8.4"
datadir    = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/share/x86_64-linux-ghc-8.8.4/wordsOwn-0.1.0.0"
libexecdir = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/libexec/x86_64-linux-ghc-8.8.4/wordsOwn-0.1.0.0"
sysconfdir = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/Haskell/wordsOwn/.stack-work/install/x86_64-linux-tinfo6/c0cd6e7df48e29e849264e83581082e36568c452c8c4cc94ee9eec72e6fbc6fc/8.8.4/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "wordsOwn_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "wordsOwn_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "wordsOwn_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "wordsOwn_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "wordsOwn_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "wordsOwn_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
